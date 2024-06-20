Run `pre-commit install` to install pre-commit into your git hooks.
pre-commit will now run on every commit.
Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do.
If you want to manually run all pre-commit hooks on a repository, `run pre-commit run --all-files`.
To run individual hooks use `pre-commit run <hook_id>`.


- id: check-merge-conflict
Description: Check that merge conflicts are not being committed

- id: debug-statements
Description: Detect accidentally committed debug statements

- id: check-builtin-literals
Description: Require literal syntax when initializing builtin types

- id: end-of-file-fixer
Description: Make sure that there is an empty line at the end

- id: mixed-line-ending
Description: Detect if mixed line ending is used (\r vs. \r\n)

- id: trailing-whitespace
Description: Remove trailing whitespace at end of line

- id: name-tests-test
Description:
verifies that test files are named correctly.
--pytest (the default): ensure tests match .*_test\.py
--pytest-test-first: ensure tests match test_.*\.py
--django / --unittest: ensure tests match test.*\.py


All common linters example:

minimum_pre_commit_version: 3.2.0

exclude: '^docs/'

default_stages: [commit, push]

default_language_version:
  python: python3.12

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-merge-conflict
      - id: debug-statements
      - id: check-builtin-literals
      - id: end-of-file-fixer
      - id: mixed-line-ending
      - id: trailing-whitespace
      - id: name-tests-test
  
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.15.1
    hooks:
      - id: pyupgrade
        args: [ --py312-plus ]

  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.9.0
    hooks:
      - id: mypy

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.10.1
    hooks:
      - id: isort

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.2
    hooks:
      # Linter
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      # Formatter
      - id: ruff-format

  - repo: https://github.com/adamchainz/django-upgrade
    rev: 1.16.0
    hooks:
      - id: django-upgrade
        args: [ "--target-version", "5.0" ]

  - repo: https://github.com/Riverside-Healthcare/djLint
    rev: v1.34.1
    hooks:
      - id: djlint-reformat-django
      - id: djlint-django
