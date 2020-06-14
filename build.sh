#!/bin/bash

py.test --collect-only tests/

## Write installed packages to requirements.txt
pip freeze > requirements.txt

## Remove cached files
find . -name '__pycache__' -type d -exec rm -r {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +

## Zip tests/ and requirements.txt into test_bundle.zip
zip -r test_bundle.zip tests/ requirements.txt
