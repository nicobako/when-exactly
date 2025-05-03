# When Exactly

An expressive datetime library for Python.

*When-Exactly* is still a work-in-progress.

Check out the documentation at [when-exactly.nicobako.me](https://when-exactly.nicobako.me).

## Development

### Setup

```bash
# windows
py -3.13 -m venv .venv
source .venv/Scripts/activate

# linux
python3.13 -m venv .venv
source .venv/bin/activate

# both
pip install -r requirements.txt
pip install -e .
pre-commit install
```

### Creating requirements

```
pip install \
  pytest \
  pytest-cov \
  mkdocs \
  pre-commit \
  build \

pip freeze > requirements.txt
```

### Testing

```bash
pytest .
```

### Documentation

```bash
# live-preview
mkdocs serve

# deploy
mkdocs gh-deploy
```