#!/usr/bin/env python

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from copy import deepcopy

import yaml
from packaging import version as packaging_version

RELEASES_OUTPUT_DIR = "releases"
MODULES_DIR = "modules"

try:
    import pypandoc
except ImportError:
    print(
        "ERROR: pypandoc is not installed. Please run: pip install pypandoc pypandoc-binary"
    )
    exit(1)


def check_dependencies():
    """Checks if docstrfmt is installed."""
    if not shutil.which("docstrfmt"):
        print("ERROR: docstrfmt command not found.")
        print("Please install it ('pip install docstrfmt')")
        exit(1)
    print("INFO: All required dependencies are present.")


def clone_or_update_repo(name, branch, dir_name, owner="openwisp"):
    """Clones or updates a module repository."""
    repository = f"{owner}/{name}"
    if os.environ.get("SSH"):
        repo_url = f"git@github.com:{repository}.git"
    else:
        repo_url = f"https://github.com/{repository}.git"
    clone_path = os.path.abspath(os.path.join(MODULES_DIR, dir_name))
    try:
        if not os.path.exists(MODULES_DIR):
            os.makedirs(MODULES_DIR)
        if os.path.exists(clone_path):
            print(f"INFO: Repository '{name}' exists. Checking out '{branch}'...")
            subprocess.run(
                ["git", "fetch"],
                cwd=clone_path,
                check=True,
                capture_output=True,
                text=True,
            )
            subprocess.run(
                ["git", "-c", "advice.detachedHead=false", "checkout", branch],
                cwd=clone_path,
                check=True,
                capture_output=True,
                text=True,
            )
        else:
            print(f"INFO: Cloning repository '{name}' on branch/tag '{branch}'...")
            subprocess.run(
                ["git", "clone", "--branch", branch, repo_url, clone_path],
                check=True,
                capture_output=True,
                text=True,
            )
    except subprocess.CalledProcessError as e:
        print(f"ERROR cloning/updating {name} to '{branch}': {e.stderr}")
        return None
    return clone_path


def _parse_rst_changelog(lines, version_string):
    """
    Extracts a specific version section from a list of RST-formatted lines.
    """
    if re.match(r"^\d+\.\d+$", version_string):
        search_version = f"{version_string}.0"
    else:
        search_version = version_string
    print(f"INFO: Searching for version '{search_version}' in RST content...")

    content, in_section = [], False
    # Match both "Version 1.1.0 [date]" and "0.2.1 [date]"
    start_regex = re.compile(r"^(?:Version )?" + re.escape(search_version) + r" \[.*")
    end_regex = re.compile(r"^(?:Version )?\d+\.\d+.*")

    for line in lines:
        if not in_section:
            if start_regex.match(line):
                in_section = True
        else:
            if end_regex.match(line):
                break
            content.append(line)
    # remove heading separator
    if content and content[0].startswith("------"):
        content = content[1:]
    return "".join(content).strip() or None


def get_changelog_content(repo_path, version_string):
    """
    Finds a changelog file, converts it to RST if needed, and returns the
    content for the specified version.
    """
    if not repo_path:
        return None, None

    changelog_options = [
        "CHANGES.rst",
        "CHANGES.md",
        "CHANGELOG.md",
        "CHANGELOG.rst",
    ]
    found_path = None
    for option in changelog_options:
        path = os.path.join(repo_path, option)
        if os.path.exists(path):
            found_path = path
            break

    if not found_path:
        return None, None

    print(f"INFO: Found changelog file: {found_path}")
    with open(found_path, "r", encoding="utf-8") as f:
        raw_content = f.read()

    rst_lines = []
    if found_path.endswith(".md"):
        print("INFO: Converting entire Markdown changelog to RST...")
        tmp_path = None
        try:
            # Convert MD to RST and format it in a temporary file
            rst_content = pypandoc.convert_text(raw_content, "rst", format="md")
            with tempfile.NamedTemporaryFile(
                mode="w+", suffix=".rst", delete=False
            ) as tmp:
                tmp_path = tmp.name
                tmp.write(rst_content)
                tmp.flush()

            subprocess.run(
                [
                    "docstrfmt",
                    "--no-docstring-trailing-line",
                    "--ignore-cache",
                    "--line-length",
                    "74",
                    tmp_path,
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            with open(tmp_path, "r", encoding="utf-8") as f:
                rst_lines = f.readlines()
        except (subprocess.CalledProcessError, RuntimeError) as e:
            print(f"WARN: Failed during MD conversion/formatting process: {e}")
            return None, None
        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
    else:  # It's an RST file
        rst_lines = raw_content.splitlines(keepends=True)
    # Parse the RST lines to find the specific version section
    version_content = _parse_rst_changelog(rst_lines, version_string)
    return version_content, os.path.basename(found_path), version_string


def merge_module_versions(modules1, modules2):
    modules1 = deepcopy(modules1)
    for module2 in modules2:
        for module1 in modules1:
            if module1["name"] == module2["name"]:
                module1.update(module2)
                break
        else:
            modules1.append(module2)
    return modules1


def get_modules(default_modules, version_modules):
    return merge_module_versions(default_modules, version_modules)


def generate_master_index_page():
    index_path = os.path.join(RELEASES_OUTPUT_DIR, "index.rst")
    print(f"\n--- Generating Master Index Page: {index_path} ---")
    release_files = [
        f.replace(".rst", "")
        for f in os.listdir(RELEASES_OUTPUT_DIR)
        if f.endswith(".rst") and f != "index.rst"
    ]
    release_files.sort(key=packaging_version.parse, reverse=True)
    with open(index_path, "w", encoding="utf-8") as f:
        title = "Release Notes"
        f.write(f"{title}\n{'=' * len(title)}\n\n")
        f.write(
            "This section contains the release notes for major OpenWISP versions.\n\n"
        )
        f.write(".. toctree::\n   :maxdepth: 1\n\n")
        for version_name in release_files:
            f.write(f"   {version_name}\n")
    print("SUCCESS: Master index page updated.")


def main(target_version):
    check_dependencies()
    print(f"\n--- Starting Release Notes Generation for Version: {target_version} ---")
    try:
        with open("config.yml", "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: `config.yml` not found. Aborting.")
        return

    version_config = next(
        (v for v in config.get("versions", []) if v["name"] == target_version), None
    )
    if not version_config:
        print(f"ERROR: Version '{target_version}' not found in config.yml. Aborting.")
        return

    if not os.path.exists(RELEASES_OUTPUT_DIR):
        os.makedirs(RELEASES_OUTPUT_DIR)

    default_modules = (
        config.get("modules", []) if not version_config.get("overwrite_modules") else []
    )
    version_modules = version_config.get("modules", [])
    final_modules = get_modules(default_modules, version_modules)
    version_branch_fallback = version_config.get("module_branch", target_version)

    all_changelogs = []
    for module in final_modules:
        module_name, branch_to_use = module["name"], module.get(
            "branch", version_branch_fallback
        )
        print(f"\n--- Processing Module: {module_name} (Version: {branch_to_use}) ---")

        repo_path = clone_or_update_repo(
            name=module_name, branch=branch_to_use, dir_name=module["dir_name"]
        )
        content, changelog_filename, version = get_changelog_content(
            repo_path, branch_to_use
        )

        if content:
            owner = module.get("owner", "openwisp")
            repo_url = f"https://github.com/{owner}/{module_name}"
            changelog_url = f"{repo_url}/blob/{branch_to_use}/{changelog_filename}"

            heading = f"{module_name} (v{version})"
            module_section = (
                f"{heading}\n"
                f"{'-' * len(heading)}\n\n"
                f"* `Module Git Repository <{repo_url}>`__.\n"
                f"* `Module Change Log <{changelog_url}>`__.\n\n"
                f"{content}"
            )
            all_changelogs.append(module_section)
        else:
            print(
                f"WARN: No changelog found for '{module_name}' matching version '{branch_to_use}'."
            )

    if all_changelogs:
        output_filename = f"{target_version}.rst"
        output_path = os.path.join(RELEASES_OUTPUT_DIR, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            title = f"OpenWISP {target_version}"
            f.write(f"{title}\n{'=' * len(title)}\n\n")
            f.write("\n\n".join(all_changelogs))
        print(f"\nSUCCESS: Aggregated release notes file generated at '{output_path}'.")
        generate_master_index_page()
    else:
        print(
            f"\nWARN: No release notes were generated for any module in version {target_version}."
        )
    print("\n--- Release Notes Generation Finished ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a single, aggregated RST release notes file for a specific OpenWISP version."
    )
    parser.add_argument(
        "version",
        nargs="?",
        default="25.10",
        help="The release version from config.yml. Defaults to '25.10'.",
    )
    args = parser.parse_args()
    main(args.version)
