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

OUTPUT_FORMATS = ["pdf", "epub", "html"]


def get_stable_version(versions):
    """
    Returns the stable version from a list of versions.
    It is assumed that the highest version is the stable version.

    If there is only one version, it is returned as stable version,
    even if it is 'dev'.

    Parameters:
        versions (list): A list of dictionaries representing versions.
            Each dictionary should have a 'name' key.

    Returns:
        str: The name of the stable version.

    This function takes a list of versions and finds the stable version
    by comparing the version names.

    Example:
        versions = [
            {'name': '1.0.0'},
            {'name': '2.0.0'},
            {'name': 'dev'},
            {'name': '3.0.0-beta'}
        ]
        get_stable_version(versions)
        # Output: '2.0.0'
    """

    def get_version_object(version):
        """
        Returns a packaging version object for the given version dictionary.
        """
        version_name = version["name"]
        # Special case for 'dev' version: we treat it as having a version
        # of '0' so that it will come as last when we perform max operation.
        if version_name == "dev":
            version_name = "0"
        return packaging_version.parse(version_name)

    if len(versions) == 1:
        return versions[0]["name"]

    stable_version = max(versions, key=get_version_object)
    return stable_version["name"]


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
            if module1["name"] == module2["name"]:
                module1.update(module2)
                break
        else:
            modules1.append(module2)
    return modules1


def get_build_versions(all_versions, output_version):
    if not output_version:
        # Build all versions
        return all_versions
    for version in all_versions:
        if version["name"] == output_version:
            return [version]


def get_modules(
    default_modules,
    version_modules,
    overridden_modules,
):
    """
    Merge module versions from default, version-specific, and overridden modules.
    The order of priority is: overridden > version-specific > default

    Args:
        default_modules (list): List of dictionaries representing default module versions.
            These modules are defined at the root of the config.yml file.
            These are common for all OpenWISP versions.
        version_modules (list): List of dictionaries representing version-specific module versions.
            These modules are defined for each OpenWISP version.
        overridden_modules (list): List of dictionaries representing overridden module versions.
            These modules are defined from the CLI.

    Returns:
        list: List of dictionaries representing merged module versions.
    """
    modules = merge_module_versions(version_modules, overridden_modules)
    modules = merge_module_versions(default_modules, modules)
    return modules


def parse_modules_arg(value):
    """
    Parses a comma-separated string of input modules and returns a dictionary
    where the keys are versions and the values are lists of dictionaries
    representing the modules.

    Args:
        value (string): A string of input modules in the format
            `version=<version>:repository=<repo-owner>/<repo-name>:dir_name=<dir-name>, ...`.

    If a module does not specify a `version`, it defaults to `'dev'`.
    The `repository` should be in the format `repo-owner/repo-name`, e.g. `openwisp/openwisp2-docs`.
    The `dir_name` is optional and defaults to the module name if not specified.
    """
    entries = value.split(",")
    result = {}
    for entry in entries:
        module = {}
        version = "dev"
        for item in entry.split(":"):
            key, value = item.split("=")
            if key == "version":
                version = value
            elif key == "repository":
                owner, name = value.split("/")
                module.update({"name": name, "owner": owner})
            else:
                module[key] = value
        try:
            result[version].append(module)
        except KeyError:
            result[version] = [module]
    return result


def parse_formats_arg(value):
    """
    Parses a comma-separated string of output formats and validates them.

    Args:
        value (str): A string of output formats separated by commas.

    Returns:
        list: A list of output formats.

    Raises:
        SystemExit: If any of the output formats are not supported.

    This function takes a comma-separated string of output formats and splits it into a list.
    It then validates each format by checking if it is in the `OUTPUT_FORMATS` list.
    If any format is not supported, it prints an error message and exits the program.
    If all formats are supported, it returns the list of output formats.
    """
    output_formats = value.split(",")
    # Validate all output formats are supported
    for format in output_formats:
        if format not in OUTPUT_FORMATS and format != "version_map":
            print(f"ERROR: {format} is not a valid output format")
            exit(2)
    return output_formats


def parse_version_arg(value):
    """
    Validates the passed version exists in the config.yml file.

    Args:
        value (str): The version to be validated.

    Returns:
        str: The validated version if it exists in the config.yml file.

    Raises:
        SystemExit: If the version is not found in the config.yml file.
    """
    # Validate passed version exists in config.yml
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    for version in config["versions"]:
        if version["name"] == value:
            return value
    print(f"ERROR: {value} is not a valid version")
    exit(3)


def create_symlink(src, dest):
    """
    Create a symbolic link from src to dest.

    If dest is not 'openwisp-docs', it will be placed inside the
    'openwisp-docs' directory.
    If a symlink already exists at the destination, it will be
    removed before creating the new one.

    Args:
        src (str): The source path to be linked from
        dest (str): The destination path to link to
    """
    if dest == "openwisp-docs":
        dest = "staging-dir"
    else:
        dest = os.path.join("staging-dir", dest)
    if os.path.islink(dest):
        os.unlink(dest)
    os.symlink(src, dest)


def remove_symlink(dest):
    """
    Remove the symbolic link at the destination path.

    Args:
        dest (str): The destination path of the symbolic link to be removed.
    """
    if dest == "openwisp-docs":
        dest = "staging-dir"
    else:
        dest = os.path.join("staging-dir", dest)
    if os.path.islink(dest):
        os.unlink(dest)


def git_is_on_branch(repo_path):
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() != "HEAD"


def clone_or_update_repo(
    name,
    branch,
    dir_name,
    skip_fetch=False,
    owner="openwisp",
    dest=None,
    version_name=None,
):
    """
    Clone or update a repository based on the module name and branch provided.
    If the repository already exists, update it. Otherwise, clone the repository.
    The resulting directory is then symlinked internally.
    If skip_fetch=True is passed, git fetching/cloning
    is skipped and only symlink is performed.
    """
    repository = f"{owner}/{name}"
    # Support for building with local changes
    if name == "openwisp-docs":
        # Ensure staging-dir is a real, empty directory
        if os.path.islink("staging-dir") or os.path.isfile("staging-dir"):
            os.unlink("staging-dir")
        elif os.path.isdir("staging-dir"):
            shutil.rmtree("staging-dir")
    # If dev version, copy all doc files to the staging dir
    if name == "openwisp-docs" and version_name == "dev":
        os.makedirs("staging-dir", exist_ok=True)
        base_dir = "docs" if os.path.isdir("docs") else "."
        exclude_items = ("staging-dir", "modules", "version_switcher")
        for item in os.listdir(base_dir):
            is_dir = os.path.isdir(os.path.join(base_dir, item))
            if any(
                (
                    # not a dir nor a rst file, nor the spelling wordlist
                    all(
                        (
                            not is_dir,
                            not item.endswith(".rst"),
                            item != "spelling_wordlist.txt",
                        )
                    ),
                    # it's a dir but not designed to contain rst files
                    is_dir and item.startswith((".", "_")),
                    # in the exclude list
                    item in exclude_items,
                )
            ):
                continue
            # skip virtual environments (detect with pyvenv.cfg)
            if os.path.isdir(os.path.join(base_dir, item)) and os.path.exists(
                os.path.join(base_dir, item, "pyvenv.cfg")
            ):
                continue
            src_path = os.path.abspath(os.path.join(base_dir, item))
            dest_path = os.path.join("staging-dir", item)
            if os.path.islink(dest_path):
                os.unlink(dest_path)
            if not os.path.exists(dest_path):
                os.symlink(src_path, dest_path)
        return
    if os.environ.get("SSH"):
        # SSH cloning is a convenient option for local development, as it
        # allows you to commit changes directly to the repository, but it
        # requires that you have added your public SSH key to your GitHub
        # account and have access to the repository. This means that it won't
        # work on GitHub Actions, and it won't work for contributors who don't
        # use SSH to access GitHub.
        repo_url = f"git@github.com:{repository}.git"
    else:
        repo_url = f"https://github.com/{repository}.git"
    # update if dir exists, otherwise clone
    clone_path = os.path.abspath(os.path.join("modules", dir_name))
    # Using refs/heads/ prefix and --no-tags to explicitly fetch branches only, not tags
    branch_ref = f"refs/heads/{branch}:refs/remotes/origin/{branch}"
    if os.path.exists(clone_path) and not skip_fetch:
        print(f"Repository '{name}' already exists. Updating...")
        subprocess.run(
            # Update remote-tracking ref (avoid fetching into checked-out branch)
            [
                "git",
                "fetch",
                "--no-tags",
                "origin",
                branch_ref,
            ],
            cwd=clone_path,
            check=True,
        )
        # "-c advice.detachedHead=false" is used to suppress the warning
        # about being in a detached HEAD state when checking out tags.
        subprocess.run(
            [
                "git",
                "-c",
                "advice.detachedHead=false",
                "checkout",
                "-B",
                branch,
                "FETCH_HEAD",
            ],
            cwd=clone_path,
            check=True,
        )
        # In CI/production environments, the repository is always freshly
        # cloned, so pulling is unnecessary and would only result in redundant
        # network calls.
        # During local development, we attempt to pull updates, but only if the
        # current HEAD is on a branch (i.e., not detached, such as when on a tag).
        if not os.environ.get("PRODUCTION", False) and git_is_on_branch(clone_path):
            subprocess.run(
                ["git", "pull", "origin", "--no-tags", branch_ref],
                cwd=clone_path,
                check=True,
            )
    elif not skip_fetch:
        print(f"Cloning repository '{name}'...")
        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--no-single-branch",
                "--no-tags",
                "--branch",
                branch,
                repo_url,
                clone_path,
            ],
            check=True,
        )
    elif skip_fetch and not os.path.exists(clone_path):
        raise FileNotFoundError(
            f'Repository "{name}" not found at {clone_path}; run without SKIP_FETCH=1 first.'
        )
    # Create a symlink to either the 'docs' directory inside the cloned repository
    # or to the entire repository if no 'docs' directory exists.
    # This makes the documentation sources available to the Sphinx build process.
    src = os.path.join(clone_path, "docs")
    if not os.path.exists(src):
        # If no 'docs' directory exists, use the entire repository
        src = clone_path
    dest = dest or dir_name
    create_symlink(src, dest)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--formats",
        type=parse_formats_arg,
        default=OUTPUT_FORMATS,
        help="comma separated output formats (pdf, epub, or html)",
    )
    parser.add_argument(
        "--version",
        type=parse_version_arg,
        default=None,
        help="document version to build",
    )
    parser.add_argument(
        "--modules",
        default={},
        type=parse_modules_arg,
        help="comma separated modules to build"
        "in the format of <version:module-name>:<branch>:<dir-name>:<repository-owner>",
    )
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        default=False,
        help="skip fetching/cloning repositories (useful for quick iteration while editing docs)",
    )
    args = parser.parse_args()
    with open("config.yml") as f:
        config = yaml.safe_load(f)
    build_versions = get_build_versions(config["versions"], args.version)
    stable_version = get_stable_version(build_versions)
    docs_root = ""
    html_base_url = ""
    build_dir = "_build"
    if os.environ.get("PRODUCTION", False):
        docs_root = "/docs"
        html_base_url = "https://openwisp.io"
        build_dir = f"{build_dir}{docs_root}"
    # loop over versions and build each one by one
    for version in build_versions:
        version_name = version["name"]
        module_dirs = []
        # Modules which are configured to be included in all the builds
        default_modules = (
            config["modules"] if not version.get("overwrite_modules") else []
        )
        # Modules which are defined for specific version
        version_modules = version.get("modules", [])
        # Modules which are defined from the command line
        overridden_modules = args.modules.get(version_name, [])
        modules = get_modules(
            default_modules=default_modules,
            version_modules=version_modules,
            overridden_modules=overridden_modules,
        )
        # If a module does not define a branch,
        # it will fallback to the version_branch.
        version_branch = version.get("module_branch", version["name"])
        docs_branch = version.get("docs_branch", "master")
        clone_or_update_repo(
            name="openwisp-docs",
            branch=docs_branch,
            skip_fetch=args.skip_fetch,
            dir_name="openwisp-docs",
            version_name=version_name,
        )
        for module in modules:
            clone_or_update_repo(
                branch=module.pop("branch", version_branch),
                skip_fetch=args.skip_fetch,
                **module,
            )
            module_dirs.append(module["dir_name"])
        sphinx_src_dir = version.get("sphinx_src_dir", "staging-dir")
        for format in ["spellcheck"] + args.formats:
            subprocess.run(
                [
                    "make",
                    format,
                    f"SRCDIR={sphinx_src_dir}",
                    f"BUILDDIR={build_dir}/{version_name}",
                ],
                env=dict(
                    os.environ,
                    DOCS_ROOT=docs_root,
                    OPENWISP2_VERSION=version_name,
                    STABLE_VERSION=stable_version,
                    HTML_BASE_URL=html_base_url,
                ),
                check=True,
            )
        # Remove all temporary directories
        for dir in module_dirs:
            remove_symlink(dir)
    # Generate the index.html file which redirects to the stable version.
    env = Environment(loader=FileSystemLoader("_static"))
    template = env.get_template("index.jinja2")
    with open(f"{build_dir}/index.html", "w") as f:
        f.write(template.render(stable_version=stable_version, docs_root=docs_root))
    # Create a symbolic link for the stable version
    subprocess.run(
        [
            "ln",
            "-rsf",
            f"{build_dir}/{stable_version}",
            f"{build_dir}/stable",
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
