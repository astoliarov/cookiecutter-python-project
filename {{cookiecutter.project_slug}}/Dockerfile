FROM python:{{cookiecutter.python_version}}-slim-buster as base

WORKDIR ${APP_DIR}

RUN apt update
RUN apt install make

COPY Makefile ${APP_DIR}/
RUN make poetry

COPY poetry.lock pyproject.toml README.md ${APP_DIR}/
COPY src/ ${APP_DIR}/src
RUN poetry config virtualenvs.create false
RUN make install


CMD ["/bin/bash"]

FROM base as testing

ARG APP_DIR

COPY .flake8 ${APP_DIR}/
COPY tests ${APP_DIR}/tests

RUN make install-dev
