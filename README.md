# About

This repository is a simple example of how to use FastAPI to build a REST API in Python.

# Setup

This project uses `uv` to manage its Python virtual environment, so make sure you have `uv` installed ([guide](https://docs.astral.sh/uv/getting-started/installation/)).

To run this project in development mode:

```bash
uv run fastapi dev src/app/main.py
```

To run this project in production mode:

```bash
uv run fastapi run src/app/main.py
```

# Building a container image

Via Podman:

```bash
podman build -t fast-api-app .
```

To run the container:

```bash
podman run -p 8000:8000 fast-api-app:latest
```
