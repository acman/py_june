#!/bin/bash

# Exit script if any command fails
set -e

source venv/bin/activate

echo "Running tests with coverage..."
coverage run -m pytest

echo "Generating coverage report..."
coverage report --fail-under=80
coverage html
