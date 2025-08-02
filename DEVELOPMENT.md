# Development Notes

## Environment Setup

```bash
# Windows
py -3.13 -m venv .venv
source .venv/Scripts/activate

# Linux
python3.13 -m venv .venv
source .venv/bin/activate

# Install dev dependecies
pip install --upgrade pytest mkdocs pre-commit
pre-commit install --install-hooks
```

## Deployment

```bash
deploy() {
    set -e  # Exit immediately if a command exits with a non-zero status
    version=$1

    # run tests and static analysis
    pytest
    pre-commit run --all-files

    # build
    mkdocs gh-deploy --strict
    python -m build

    # tag and deploy
    git tag -a "$version" -m "$version"
    python -m twine upload --repository pypi dist/*
    git push --all
}
```

## Date and Time Format

- [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
- [Extended Date Time Format](https://www.loc.gov/standards/datetime/)
