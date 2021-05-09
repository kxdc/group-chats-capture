
# Steps to upgrade

## Setting up as a Python project using Poetry

```bash
source ~/.poetry/env
poetry init --no-interaction
```

A file named `pyproject.toml` will be created, this is the new Python package
config file specified in [PEP 517](https://www.python.org/dev/peps/pep-0517/)
and [PEP 518](https://www.python.org/dev/peps/pep-0518/).

```bash
vim ./pyproject.toml
```

Supplement `./pyproject.toml` with more metadata such as `description`,
`license`, `readme`, `homepage` and so on.

## Creating a package in src layout

## Managing virtual environments with Poetry

## Managing dependencies with Poetry

## Command-line interfaces with click

