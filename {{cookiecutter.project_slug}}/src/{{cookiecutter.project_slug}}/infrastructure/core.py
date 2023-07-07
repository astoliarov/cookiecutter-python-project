from {{cookiecutter.project_slug}}.infrastructure.logs import setup_logs
from {{cookiecutter.project_slug}}.infrastructure.sentry import setup_sentry


def setup_infrastructure() -> None:
    setup_logs()
    setup_sentry()
