#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

LIMIT = 75


def check_url(line):
    """
    Check if there is a url present in the given line
    """
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url = re.findall(pattern, line)
    return bool(url)


def check_line_length(file_path):
    """
    Ensures line length of lines in file specified in ``file_path`` are lower than ``LIMIT``,
    interrupts execution with exit code 1 otherwise
    """
    file = file_path.split('/')[-1]
    with open(file_path) as f:
        lines = f.readlines()
    for (line_number, line) in enumerate(lines, start=1):
        length = len(line)
        if length > LIMIT and check_url(line) is not True:
            print('line {} in file {} is longer '
                  'than {} characters'.format(line_number, file, LIMIT))
            sys.exit(1)


def main():
    current_path = os.getcwd()
    file_paths = glob.glob(current_path + '/**/*.rst')
    for file_path in file_paths:
        check_line_length(file_path)


if __name__ == '__main__':
    main()
