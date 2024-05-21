#!/usr/bin/env python

# This script generates the documentation for all the OpenWISP versions
# defined in config.yml. For each version, it will clone or update the
# OpenWISP modules and checkout the specified branch. It will then generate
# the documentation using Sphinx in a separate directory for each
# OpenWISP version.

import os
import shutil
import subprocess
import sys

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


def merge_module_versions(default_modules, version_modules):
    modules = default_modules.copy()
    for version_module in version_modules:
        for module in modules:
            if module['name'] == version_module['name']:
                module.update(version_module)
    return modules


def clone_or_update_repo(module_name, branch, dir_name, is_production=False):
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
        repo_url = f'git@github.com:openwisp/{module_name}.git'
    else:
        repo_url = f'https://github.com/openwisp/{module_name}.git'
    repo_path = os.path.join('modules', dir_name)

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
        subprocess.run(
            ['git', 'sparse-checkout', 'init', '--cone'], cwd=repo_path, check=True
        )
        subprocess.run(
            ['git', 'sparse-checkout', 'set', 'docs'], cwd=repo_path, check=True
        )
    subprocess.run(
        [
            'cp',
            '-r',
            os.path.join(repo_path, 'docs'),
            dir_name,
        ],
        check=True,
    )


def main():
    PRODUCTION = os.environ.get('PRODUCTION', False)
    with open('config.yml') as f:
        config = yaml.safe_load(f)
    stable_version = get_stable_version(config['versions'])

    docs_root = ''
    if PRODUCTION:
        docs_root = '/docs/__new__'
    os.environ['DOCS_ROOT'] = docs_root
    os.environ['STABLE_VERSION'] = stable_version

    output_formats = OUTPUT_FORMATS.copy()
    if len(sys.argv) > 1:
        output_formats = sys.argv[1].split(',')
        for format in output_formats:
            if format not in OUTPUT_FORMATS:
                print(f'ERROR: {format} is not a valid output format')

    for version in config['versions']:
        module_dirs = []
        version_modules = version.get('modules', [])
        if version_modules is not False:
            modules = merge_module_versions(config['modules'], version_modules)
            branch = version.get('branch', version['name'])
            for module in modules:
                clone_or_update_repo(
                    module['name'],
                    module.get('branch', branch),
                    module['dir_name'],
                    PRODUCTION,
                )
                module_dirs.append(module['dir_name'])
        version_name = version['name']

        os.environ['OPENWISP2_VERSION'] = version_name
        for format in output_formats:
            subprocess.run(
                ['make', format, f'BUILDDIR=_build/{version_name}'], check=True
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
            '-rs',
            f'_build/{stable_version}',
            '_build/stable',
        ],
        check=True
    )

if __name__ == "__main__":
    main()
