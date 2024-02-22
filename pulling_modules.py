import os
import shutil
import subprocess

import yaml


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

    for version in config['versions']:
        for module in version['modules']:
            module_name = module['name']
            branch = module['branch']
            clone_or_update_repo(module_name, branch)
        version_name = version['name']

        os.makedirs(f'_build/{version_name}', exist_ok=True)
        os.environ['OPENWISP2_VERSION'] = version_name
        subprocess.run(
            ['sphinx-build', '-b', 'html', '.', f'_build/{version_name}'], check=True
        )
    shutil.copy('_static/index.html', '_build/index.html')


if __name__ == "__main__":
    main()
