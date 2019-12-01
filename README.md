# f-cli

A CLI tool packed with commands designed to simplify the workflow of a Cloud Engineer.

## Development

### Commands

| Command               | Description                            |
|-----------------------|----------------------------------------|
| `make deploy <env>`   | Execute runway for a given environment |
| `make destroy <env>`  | Execute runway for a given environment |
| `make plan <env>`     | Execute runway for a given environment |
| `make sync`           | Sync python environment with pipfile   |

### Setup

This section outlines how to setup portions of the repo that cannot be reasonably automated.

#### Development Environment

1. `export $(cat .env | xargs)` to setup environment variables.
2. `make sync` or `pipenv sync --dev --three` after completing **Step 1**.
