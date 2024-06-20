## Docs:
#### flake8: https://flake8.pycqa.org
#### black: https://black.readthedocs.io
#### isort: https://pycqa.github.io/isort
#### ruff: https://docs.astral.sh/ruff
#### mypy: https://mypy.readthedocs.io

## Base linters commands:

`flake8 .`

`black . --diff`

`isort . --diff`

`ruff check .`
`ruff format . --diff`

`mypy .`

Default config for black, flake8, isort

# BLACK pyproject.toml
[tool.black]
line-length = 99
target-version = ['py312']
extend-exclude = '''
(
  migrations
  | .cache
  | venv
)
'''

# ISORT pyproject.toml
[tool.isort]
profile = "black"
line_length = 99
extend_skip = [
    ".cache",
    "venv",
]

# FLAKE8 setup.cfg
[flake8]
max-line-length = 99
extend-ignore = E203,E701,F401,F403,E501
max-complexity = 10
exclude = migrations, .cache, venv
