# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Development

### Local

Tools that you will need:

- Python >= {{cookiecutter.python_version}}
- Virtualenv
- pyenv (https://github.com/pyenv/pyenv)
- pyenv-virtualenv (https://github.com/pyenv/pyenv-virtualenv)
- direnv (https://direnv.net/) - optional

#### How to prepare Python version and virtualenv

1. Install pyenv https://github.com/pyenv/pyenv
2. Install pyenv virtualenv https://github.com/pyenv/pyenv-virtualenv
3. Install python {{cookiecutter.python_version}} `pyenv install {{cookiecutter.python_version}}`
4. Create virtualenv `pyenv virtualenv {{cookiecutter.python_version}} {{cookiecutter.project_slug}}`
6. Ensure that you have `make` installed

#### App installation

Run all commands inside project directory

1. Activate your environment created at previous step
2. Install poetry `make poetry`
3. Install dependencies + dev dependencies `make install-dev`

Now you are ready to run app or tests

#### Tests

- run all tests `make test`
- run only unit `make test/unit`
- run only integration `make tests/integration`