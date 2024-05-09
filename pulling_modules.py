import os
import subprocess

import yaml
from jinja2 import Environment, FileSystemLoader


def clone_or_update_repo(module_name, branch):
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

    for version in config['versions']:
        for module in version['modules']:
            module_name = module['name']
            branch = module['branch']
            clone_or_update_repo(module_name, branch)
        version_name = version['name']

        os.environ['OPENWISP2_VERSION'] = version_name
        subprocess.run(
            ['sphinx-build', '-b', 'html', '.', f'_build/{version_name}'], check=True
        )
        # subprocess.run(
        #     ['sphinx-build', '-b', 'pdf', '.', f'_build/{version_name}'], check=True
        # )
        # subprocess.run(
        #     ['sphinx-build', '-b', 'epub', '.', f'_build/{version_name}'], check=True
        # )

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
