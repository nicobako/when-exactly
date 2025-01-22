# When Exactly

The precisely ambiguous time frame library.

## Development Notes

### Uploading to pypi

```bash
python -m build
python -m twine upload --repository pypi dist/*
```

### Building documentation

```bash
mkdocs gh-deploy
git push --all
```

### Date and Time Format

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
[Extended Date Time Format](https://www.loc.gov/standards/datetime/)