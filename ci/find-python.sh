#!/usr/bin/env bash

set -e

find . -type f \
	-name "*.py" -regex '.*\(src\)/.*' \
	-exec "$@" {} +
