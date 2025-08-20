# When Exactly

An expressive datetime library for Python.

*When-Exactly* is still a work-in-progress.

Check out the documentation at [when-exactly.nicobako.me](https://when-exactly.nicobako.me).

## Development

### Setup

Instructions for setting up the dev environment.

```bash
uv sync --all-groups
uv run pre-commit install
```

### Linting

All linting and static analysis is run by pre-commit.

```bash
uv run pre-commit run --all-files
```

### Testing

Use pytest.

```bash
uv run pytest .
```

### Documentation

Documentation is built using mkdocs.

```bash
# live-preview
uv run mkdocs serve

# deploy
uv run mkdocs gh-deploy
```

## Deploy

```bash
deploy () {
    set -e  # Exit immediately if a command exits with a non-zero status
    version=$1

    # run tests and static analysis
    uv run pre-commit run --all-files
    uv run pytest .

    # build
    uv run mkdocs gh-deploy --strict
    uv build

    # tag and deploy
    uv version "$version"
    git commit -am "Version $verion"
    git tag -a "$version" -m "$version"
    git push --all
    uvx uv-publish@latest
}

```
