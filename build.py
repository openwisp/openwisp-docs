#!/usr/bin/env python

# This script generates the documentation for all the OpenWISP versions
# defined in config.yml. For each version, it will clone or update the
# OpenWISP modules and checkout the specified branch. It will then generate
# the documentation using Sphinx in a separate directory for each
# OpenWISP version.

import argparse
import os
import shutil
import subprocess
from copy import deepcopy

import yaml
from jinja2 import Environment, FileSystemLoader
from packaging import version as packaging_version

OUTPUT_FORMATS = ['pdf', 'epub', 'html']


def get_stable_version(versions):
    def get_version_object(version):
        version_name = version['name']
        if version_name == 'dev':
            version_name = '0'
        return packaging_version.parse(version_name)

    stable_version = max(versions, key=get_version_object)
    return stable_version['name']


def merge_module_versions(modules1, modules2):
    """
    Merges two lists of module versions, combining them based on the 'name' key.

    Args:
        modules1 (list): A list of dictionaries representing module versions.
        modules2 (list): A list of dictionaries representing module versions.

    Returns:
        list: A new list of dictionaries representing the merged module versions.

    The function takes two lists of dictionaries representing module versions,
    where each dictionary has a 'name' key. It merges the two lists by comparing
    the 'name' keys of the dictionaries. If a dictionary with the same 'name' key
    is found in both lists, the function updates the values of the dictionary in
    the first list with the values from the dictionary in the second list. If a
    dictionary with the same 'name' key is not found in the first list, the
    function appends the dictionary from the second list to the first list.

    The function returns a new list of dictionaries representing the merged module
    versions.
    """
    modules1 = deepcopy(modules1)
    for module2 in modules2:
        for module1 in modules1:
            if module1['name'] == module2['name']:
                module1.update(module2)
                break
        else:
            modules1.append(module2)
    return modules1


def get_modules(
    default_modules,
    version_modules,
    overridden_modules,
):
    modules = merge_module_versions(version_modules, overridden_modules)
    modules = merge_module_versions(default_modules, modules)
    return modules


def parse_input_modules(value):
    entries = value.split(',')
    result = {}
    for entry in entries:
        module = {}
        version = 'dev'
        for item in entry.split(':'):
            key, value = item.split('=')
            if key == 'version':
                version = value
            else:
                module[key] = value
        try:
            result[version].append(module)
        except KeyError:
            result[version] = [module]
    return result


def clone_or_update_repo(module_name, branch, dir_name, owner='openwisp'):
    """
    Clone or update a repository based on the module name and branch provided.
    If the repository already exists, update it. Otherwise, clone the repository.
    """
    if os.environ.get('DEV'):
        # SSH cloning is a convenient option for local development, as it
        # allows you to commit changes directly to the repository, but it
        # requires that you have added your public SSH key to your GitHub
        # account and have access to the repository. This means that it won't
        # work on GitHub Actions, and it won't work for contributors who don't
        # use SSH to access GitHub.
        repo_url = f'git@github.com:{owner}/{module_name}.git'
    else:
        repo_url = f'https://github.com/openwisp/{module_name}.git'
    repo_path = os.path.join('m+odules', dir_name)

    if os.path.exists(repo_path):
        print(f"Repository '{module_name}' already exists. Updating...")
        subprocess.run(
            ['git', 'remote', 'set-branches', 'origin', branch],
            cwd=repo_path,
            check=True,
        )
        subprocess.run(
            ['git', 'fetch', '--update-shallow', 'origin', branch],
            cwd=repo_path,
            check=True,
        )
        subprocess.run(['git', 'checkout', branch], cwd=repo_path, check=True)
    else:
        print(f"Cloning repository '{module_name}'...")
        subprocess.run(
            [
                'git',
                'clone',
                '--single-branch',
                '--branch',
                branch,
                '--depth',
                '1',
                repo_url,
                repo_path,
            ],
            check=True,
        )
        # subprocess.run(
        #     ['git', 'sparse-checkout', 'init', '--cone'], cwd=repo_path, check=True
        # )
        # subprocess.run(
        #     ['git', 'sparse-checkout', 'set', 'docs'], cwd=repo_path, check=True
        # )
    # If the module contains a doc directory, copy it to the dir_name in the root.
    # Otherwise, copy the entire directory.
    try:
        shutil.copytree(os.path.join(repo_path, 'docs'), dir_name)
    except FileNotFoundError:
        shutil.copytree(repo_path, dir_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--formats',
        default=','.join(OUTPUT_FORMATS),
        help='comma separated output formats (pdf, epub, or html)',
    )
    parser.add_argument('--version', default=None, help='document version to build')
    parser.add_argument(
        '--modules',
        default={},
        type=parse_input_modules,
        help='comma separated modules to build'
        'in the format of <version:module-name>:<branch>:<dir-name>:<repository-owner>',
    )
    args = parser.parse_args()

    PRODUCTION = os.environ.get('PRODUCTION', False)
    with open('config.yml') as f:
        config = yaml.safe_load(f)

    output_version = args.version
    if output_version:
        stable_version = output_version
    else:
        stable_version = get_stable_version(config['versions'])

    docs_root = ''
    if PRODUCTION:
        docs_root = '/docs/__new__'
    os.environ['DOCS_ROOT'] = docs_root
    os.environ['STABLE_VERSION'] = stable_version

    output_formats = args.formats.split(',')
    # Validate all output formats are supported
    for format in output_formats:
        if format not in OUTPUT_FORMATS:
            print(f'ERROR: {format} is not a valid output format')
            exit(2)

    for version in config['versions']:
        # Build documentation for all versions if output_version
        # is not specified. Otherwise, build documentation for
        # the specified version.
        if output_version and output_version != version['name']:
            continue
        version_name = version['name']
        module_dirs = []

        # Modules which are configured to be included in all the builds
        default_modules = (
            config['modules'] if not version.get('overwrite_modules') else []
        )
        # Modules which are defined for specific version
        version_modules = version.get('modules', [])
        # Modules which are defined from the command line
        overridden_modules = args.modules.get(version_name, [])
        modules = get_modules(
            default_modules=default_modules,
            version_modules=version_modules,
            overridden_modules=overridden_modules,
        )
        branch = version.get('branch', version['name'])
        for module in modules:
            clone_or_update_repo(
                module['name'],
                module.get('branch', branch),
                module['dir_name'],
            )
            module_dirs.append(module['dir_name'])

        os.environ['OPENWISP2_VERSION'] = version_name
        sphinx_src_dir = version.get('sphinx_src_dir', '.')
        for format in output_formats:
            subprocess.run(
                [
                    'make',
                    format,
                    f'SRCDIR={sphinx_src_dir}',
                    f'BUILDDIR=_build/{version_name}',
                ],
                check=True,
            )
        # Remove all temporary directories
        for dir in module_dirs:
            shutil.rmtree(dir)

    # Generate the index.html file which redirects to the stable version.
    env = Environment(loader=FileSystemLoader('_static'))
    template = env.get_template('index.jinja2')
    with open('_build/index.html', 'w') as f:
        f.write(template.render(stable_version=stable_version, docs_root=docs_root))

    # Create a symbolic link for the stable version
    subprocess.run(
        [
            'ln',
            '-rsf',
            f'_build/{stable_version}',
            '_build/stable',
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
