SHELL=/bin/bash
PYTHON_VERSION=3.11

.PHONY: format
format: format-python

.PHONY: lint
lint: lint-python

.PHONY: test
test: test-python

.PHONY: format-python
format-python:
	ci/format-python.sh

.PHONY: test-python
test-python:
	ci/test-python.sh