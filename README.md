# Cookiecutter-FastAPI-Worker-Project

Time-saving project generator for Python services for faster 🚀

It creates FastAPI APIs with built-in support for asynchronous background workers. 

## 🛠️ Features of generated project
- Separate package for business logic + tests
- FastAPI API + tests + 2 deployment options
- Background worker
- Structured logging out of the box
- Environment configuration
- Dockerfile for tests and for deploy
- Set of linters/formatters: black, isort, flake8 and mypy
- Poetry package management
- Makefile with set of commands to install, format, lint, test (on local machine and in docker)

## 🌐 Project generation
1. Install [cookiecutter tool](https://github.com/cookiecutter/cookiecutter) (with virtualenv or pyenv)
2. Generate project
    ```bash
    cookiecutter https://github.com/astoliarov/cookiecutter-python-project
    ```
### 📝  Project variables
- `project_name` - The name of the project
- `project_slug` - The development friendly name of the project. By default, based on the project name
- `project_short_description` - The description of the project. Should be human friendly
- `full_name` - Name of the author
- `email` - Email of the author
- `version` - Version of the project
- `python_version` - Python version that will be used in project
