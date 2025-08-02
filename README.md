# When Exactly

An expressive datetime library for Python.

*When-Exactly* is still a work-in-progress.

Check out the documentation at [when-exactly.nicobako.me](https://when-exactly.nicobako.me).

## Development

### Setup

```bash
uv sync
uv run pre-commit install
```

### Testing

```bash
uv run pytest .
```

### Documentation

```bash
# live-preview
uv run mkdocs serve

# deploy
uv run mkdocs gh-deploy
```

## Build

```bash
uv build
uvx uv-publish@latest
```
