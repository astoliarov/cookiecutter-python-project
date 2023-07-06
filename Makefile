POETRY ?= poetry

###########################
# Environment configuration
###########################

.PHONY: poetry/install
poetry/install:
	pip install poetry==1.5.1

.PHONY: poetry
poetry: poetry/install

.PHONY: install
install:
	$(POETRY) install


.PHONY: environment/install
poetry: poetry install


############
# Generation
############

.PHONY: generate
generate:
	python -m cookiecutter . --no-input