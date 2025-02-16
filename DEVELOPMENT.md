# Development Notes

## Deployment

```bash
deploy() {
    set -e  # Exit immediately if a command exits with a non-zero status
    version=$1

    # run tests and static analysis
    pytest
    pre-commit run --all-files

    # build
    mkdocs gh-deploy
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