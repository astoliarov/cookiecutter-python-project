POETRY ?= poetry

###########################
# Environment configuration
###########################

.PHONY: poetry/install
poetry/install:
	pip install poetry==1.5.1
	$(POETRY) config virtualenvs.create false

.PHONY: poetry
poetry: poetry/install

.PHONY: install
install:
	$(POETRY) install

.PHONY: environment/install
environment/install: poetry install


############
# Generation
############

.PHONY: generate
generate:
	python -m cookiecutter . --no-input