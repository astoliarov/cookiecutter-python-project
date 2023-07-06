POETRY ?= poetry
LINT_SOURCES_DIRS = src tests

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
	$(POETRY) install --without dev

.PHONY: install-dev
install-dev:
	$(POETRY) install

.PHONY: env/prepare
env/prepare:
	cp .env.example .env
	cp .envrc.example .envrc

##################
# Code style tools
##################
.PHONY: lint/black
lint/black:
	@echo "\033[92m< linting using black...\033[0m"
	$(POETRY) run black --check --diff $(LINT_SOURCES_DIRS)
	@echo "\033[92m> done\033[0m"
	@echo

.PHONY: lint/flake8
lint/flake8:
	@echo "\033[92m< linting using flake8...\033[0m"
	$(POETRY) run flake8 $(LINT_SOURCES_DIRS)
	@echo "\033[92m> done\033[0m"
	@echo

.PHONY: lint/isort
lint/isort:
	@echo "\033[92m< linting using isort...\033[0m"
	$(POETRY) run isort --check-only --diff $(LINT_SOURCES_DIRS)
	@echo "\033[92m> done\033[0m"
	@echo

.PHONY: lint/mypy
lint/mypy:
	@echo "\033[92m< linting using mypy...\033[0m"
	$(POETRY) run mypy --show-error-codes --skip-cache-mtime-checks $(LINT_SOURCES_DIRS)
	@echo "\033[92m> done\033[0m"
	@echo

.PHONY: lint
lint: lint/black lint/isort lint/flake8 lint/mypy

.PHONY: fmt/black
fmt/black:
	@echo "\033[92m< formatting using black...\033[0m"
	$(POETRY) run black $(LINT_SOURCES_DIRS)
	@echo "\033[92m> done\033[0m"
	@echo

.PHONY: fmt/isort
fmt/isort:
	@echo "\033[92m< formatting using isort...\033[0m"
	$(POETRY) run isort $(LINT_SOURCES_DIRS)
	@echo "\033[92m> done\033[0m"
	@echo

.PHONY: fmt
fmt: fmt/black fmt/isort

#########
# Testing
#########

.PHONY: test/unit
test/unit: TESTS ?= tests/unit
test/unit:
	$(POETRY) run python -m pytest -vv $(TESTS)

.PHONY: test/integration
test/integration: TESTS ?= tests/integration
test/integration:
	$(POETRY) run python -m pytest -vv $(TESTS)

.PHONY: test
test: test/unit test/integration

#############
# Entrypoints
#############

.PHONY: run/server
run/server:
	$(POETRY) run python -m {{cookiecutter.project_slug}}.api

.PHONY: run/worker
run/worker:
	$(POETRY) run python -m {{cookiecutter.project_slug}}.worker

##################
# Local deployment
##################
ENV_FILE ?= .env

.PHONY: local-deploy/application/up
local-deploy/application/up:
	docker-compose \
	--env-file=$(ENV_FILE) \
	--project-name {{cookiecutter.project_slug}} \
	--file docker-compose.yml \
	--profile application \
	--profile infrastructure \
	up --detach

.PHONY: local-deploy/application/stop
local-deploy/application/stop:
	docker-compose \
	--env-file=$(ENV_FILE) \
	--project-name {{cookiecutter.project_slug}} \
	--file docker-compose.yml \
	--profile application \
	--profile infrastructure \
	stop

.PHONY: local-deploy/application/down
local-deploy/application/down:
	docker-compose \
	--env-file=$(ENV_FILE) \
	--project-name {{cookiecutter.project_slug}} \
	--file docker-compose.yml \
	--profile application \
	--profile infrastructure \
	down

##########
### Docker
##########

IMAGE ?={{cookiecutter.project_slug}}
TAG ?= latest


.PHONY: docker/build
docker/build:
	docker build . \
	--tag $(IMAGE):latest \
	--target base \
	--file ./Dockerfile
	docker build . \
	--tag $(IMAGE):latest-testing \
	--target testing \
	--file ./Dockerfile

.PHONY: docker/tag
docker/tag:
	docker tag $(IMAGE):latest $(IMAGE):$(TAG)

#####################
### In-docker testing
#####################

.PHONY: in-docker/test/unit
in-docker/test/unit:
	docker run --rm \
	--env-file=$(ENV_FILE) \
	$(IMAGE):latest-testing \
	make test/unit

.PHONY: in-docker/test/integration
in-docker/test/integration:
	docker run --rm \
	--env-file=$(ENV_FILE) \
	$(IMAGE):latest-testing \
	make test/integration


.PHONY: in-docker/test
in-docker/test: docker/build docker/tag in-docker/test/unit in-docker/test/integration
