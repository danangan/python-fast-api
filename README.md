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

# Running a PostgreSQL database

A `compose.yaml` file is provided to spin up a local PostgreSQL database. It works with both Docker and Podman.

Via Podman:

```bash
podman compose up -d
```

Via Docker:

```bash
docker compose up -d
```

By default the database is available at `postgresql://postgres:postgres@localhost:5432/app`. The user, password, database name and host port can be overridden with the `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` and `POSTGRES_PORT` environment variables (or in a `.env` file).

Data is persisted in the `postgres-data` volume. To stop the database:

```bash
podman compose down      # or: docker compose down
```

To stop it and remove all data:

```bash
podman compose down -v   # or: docker compose down -v
```
