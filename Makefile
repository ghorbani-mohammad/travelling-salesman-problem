SHELL=/bin/bash
PYTHON_VERSION=3.11

.PHONY: format
format: format-python

.PHONY: lint
lint: lint-python

.PHONY: format-python
format-python:
	ci/format-python.sh

.PHONY: lint-python
lint-python:
	@MYPYPATH=social ci/lint-python.sh
