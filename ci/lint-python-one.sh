#!/usr/bin/env bash

set -e

black -t py38 --check "$@"
pylint --rcfile .pylintrc "$@"
