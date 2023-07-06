FROM python:{{cookiecutter.python_version}}-slim-buster as base

WORKDIR /app

RUN apt update
RUN apt install make

COPY Makefile /app/
RUN make poetry

COPY poetry.lock pyproject.toml README.md /app/
COPY src/ /app/src
RUN poetry config virtualenvs.create false
RUN make install


CMD ["/bin/bash"]

FROM base as testing

COPY .flake8 /app/
COPY tests /app/tests

RUN make install-dev
