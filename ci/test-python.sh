#!/usr/bin/env bash

set -e

python -m unittest $(find . -type f -name "*.py" -regex '.*\src/.*/tests/.*')
