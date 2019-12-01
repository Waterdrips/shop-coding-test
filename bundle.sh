#! /bin/bash/
set -e

# This is to be run from a parent directory, where the project exists in the shop-coding-test folder
zip -x *.idea* *venv* *.coverage* -r shop-coding-test.zip shop-coding-test/

