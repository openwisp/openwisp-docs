#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

LIMIT_TEXT = 75
LIMIT_CODE = 114


def should_skip_check(line):
    """
    Check if there is a pattern in this line
    that indicates we should skip the check
    """
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url = re.findall(pattern, line)
    return '"contents": "' in line or bool(url)


def check_line_length(file_path):
    """
    Ensures line length of lines in file specified in ``file_path`` are lower than ``LIMIT``,
    interrupts execution with exit code 1 otherwise
    """
    file = file_path.split('/')[-1]
    limit_type = 'text'
    limit = 0
    errors = []
    with open(file_path) as f:
        lines = f.readlines()
    for (line_number, line) in enumerate(lines, start=1):
        # special cases to ignore
        text = line.strip()
        if (
            text.startswith('<a')
            or text.startswith('&#115')
            or text.startswith('allow="')
        ):
            continue
        is_code = re.search(r'code-block', line)
        if is_code:
            limit_type = 'code'
            check_first_character = False
        if limit_type == 'code':
            limit = LIMIT_CODE
            if check_first_character:
                leading_spaces = len(line) - len(line.lstrip())
                if not leading_spaces and len(line) > 1:
                    limit_type = 'text'
                    limit = LIMIT_TEXT
        else:
            limit_type = 'text'
            limit = LIMIT_TEXT
        length = len(line)
        if length > limit and should_skip_check(line) is not True:
            errors.append(
                'line {} in file {} is longer '
                'than {} characters'.format(line_number, file, limit)
            )
        check_first_character = True
    if len(errors):
        body = 'The document line length exceeds the right limit.\n'
        body += 'Please check the length of the document.\n\n'
        for error in errors:
            body += '- {}\n'.format(error)
        print(body)
        sys.exit(1)


def main():
    current_path = os.getcwd()
    file_paths = glob.glob(current_path + '/**/*.rst')
    for file_path in file_paths:
        check_line_length(file_path)


if __name__ == '__main__':
    main()
