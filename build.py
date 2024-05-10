#!/usr/bin/python3

# This script generates the documentation for all the OpenWISP versions
# defined in config.yml. For each version, it will clone or update the
# OpenWISP modules and checkout the specified branch. It will then generate
# the documentation using Sphinx in a separate directory for each
# OpenWISP version.

import os
import subprocess
import sys

import yaml
from jinja2 import Environment, FileSystemLoader

OUTPUT_FORMATS = ['pdf', 'epub', 'html']


def clone_or_update_repo(module_name, branch):
    """
    Clone or update a repository based on the module name and branch provided.
    If the repository already exists, update it. Otherwise, clone the repository.
    """
    repo_url = f'https://github.com/openwisp/{module_name}.git'
    repo_path = f'modules/{module_name}'

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


def main():
    with open('config.yml') as f:
        config = yaml.safe_load(f)

    docs_root = ''
    if os.environ.get('PRODUCTION', False):
        docs_root = '/docs/__new__'
    os.environ['DOCS_ROOT'] = docs_root

    output_formats = OUTPUT_FORMATS.copy()
    if len(sys.argv) > 1:
        output_formats = sys.argv[1].split(',')
        for format in output_formats:
            if format not in OUTPUT_FORMATS:
                print(f'ERROR: {format} is not a valid output format')

    for version in config['versions']:
        for module in version['modules']:
            module_name = module['name']
            branch = module['branch']
            clone_or_update_repo(module_name, branch)
        version_name = version['name']

        os.environ['OPENWISP2_VERSION'] = version_name
        for format in output_formats:
            subprocess.run(
                ['make', format, f'BUILDDIR=_build/{version_name}'], check=True
            )

    # Generate the index.html file which redirects to the stable version.
    env = Environment(loader=FileSystemLoader('_static'))
    template = env.get_template('index.jinja2')
    with open('_build/index.html', 'w') as f:
        f.write(
            template.render(
                stable_version=config['stable_version'], docs_root=docs_root
            )
        )


if __name__ == "__main__":
    main()
