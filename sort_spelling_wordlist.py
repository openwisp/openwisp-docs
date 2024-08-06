#!/usr/bin/env python

import argparse
import hashlib
import sys


def calculate_md5(content):
    """Calculate the MD5 hash of the given content."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def sort_and_clean_file(file_path):
    """Sort, deduplicate, and clean lines in the file, then write changes if necessary."""
    with open(file_path, 'r') as file_:
        lines = file_.readlines()

    # Remove blank lines and strip leading/trailing whitespace
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    # Remove duplicates while preserving the original case
    unique_lines = list(dict.fromkeys(cleaned_lines))

    # Sort lines case-insensitively but preserve their original case
    sorted_lines = sorted(unique_lines, key=str.lower)

    # import ipdb; ipdb.set_trace()

    # Prepare content strings
    original_content = ''.join(lines)
    new_content = '\n'.join(sorted_lines)
    new_content.strip()
    new_content += '\n'

    original_md5 = calculate_md5(original_content)
    new_md5 = calculate_md5(new_content)

    # Write the file only if there's a change
    if original_md5 != new_md5:
        with open(file_path, 'w') as file:
            file.write(new_content)
        return True  # Indicates changes were made

    return False  # Indicates no changes were made


def main():
    """Main function to handle argument parsing and call the sorting function."""
    parser = argparse.ArgumentParser(description='Sort and clean lines in a text file.')
    parser.add_argument(
        '--qa',
        action='store_true',
        help='If true, script will exit with 1 if there\'s any change to spelling_wordlist.txt.',
    )

    args = parser.parse_args()
    changes_made = sort_and_clean_file('./spelling_wordlist.txt')

    if args.qa and changes_made:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
