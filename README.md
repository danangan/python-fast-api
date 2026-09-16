# About

This repository is a simple example on how to use FastAPI to build a simple REST API in in Python.

# Setup

This project uses uv to manage its python virtual environment, so make sure you have uv installed ([guide](https://docs.astral.sh/uv/getting-started/installation/)).

To run this project in development mode, simply run:

```bash
uv run fastapi dev src/app/main.py
```

To run this project in production mode, run:

```bash
uv run fastapi run src/app/main.py
```