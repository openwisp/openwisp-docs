#!/bin/bash
# Install documentation build and QA dependencies for CI and review.
set -e
if [ "${CI_SYSTEM_DEPS_READY:-0}" != 1 ]; then
    sudo apt update
    sudo apt install -y libcairo2-dev poppler-utils
    sudo npm install -g prettier
fi
if [ "${CI_SYSTEM_DEPS_ONLY:-0}" = 1 ]; then
    exit 0
fi
python -m pip install -U pip wheel setuptools
python -m pip install -U -r requirements.txt
