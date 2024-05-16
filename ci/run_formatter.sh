#!/bin/bash
set -e

poetry run black --check --diff myrepo
