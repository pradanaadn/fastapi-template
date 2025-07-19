# FastAPI Template

A minimal, production-ready FastAPI template designed to kickstart any Python web API project.

## Features

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs.
- **Scalar Docs**: Integrated [Scalar](https://scalar.com/) API documentation at `/scalar/docs`.
- **Dockerized**: Ready-to-use `Dockerfile` and `docker-compose.yaml` for local development and deployment.
- **Pre-commit Hooks**: Automated code quality checks using [pre-commit](https://pre-commit.com/).
- **Development Tools**: Includes `pytest`, `coverage`, and other useful dev dependencies.
- **Observability**: Comes with [Grafana](https://grafana.com/), [Loki](https://grafana.com/oss/loki/), and [Promtail](https://grafana.com/docs/loki/latest/clients/promtail/) for logging and monitoring.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Quick Start

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd fastapi-template
   ```

2. **Run with Docker Compose:**

   ```sh
   make run-docker
   ```

3. **Access the API:**

   - Main API: [http://localhost:8000](http://localhost:8000)
   - Scalar Docs: [http://localhost:8000/scalar/docs](http://localhost:8000/scalar/docs)
   - Grafana: [http://localhost:3000](http://localhost:3000) (default credentials: `admin`/`admin`)

4. **Stop the services:**

   ```sh
   make down-docker
   ```

## Development

- Install dependencies:

  ```sh
  uv sync --dev
  ```

- Run locally:

  ```sh
  uv icorn main:app --reload
  ```

- Run tests:

  ```sh
  pytest
  ```

## Customization

- Add your API endpoints in [`main.py`](main.py).
- Update dependencies in [`pyproject.toml`](pyproject.toml).
- Configure pre-commit hooks in [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

### Pre-commit Setup

To enable automated code quality checks before each commit, install and set up pre-commit:

```sh
uv add pre-commit
uv run pre-commit install
```

You can manually run all pre-commit hooks on all files with:

```sh
uv run pre-commit run --all-files
```
