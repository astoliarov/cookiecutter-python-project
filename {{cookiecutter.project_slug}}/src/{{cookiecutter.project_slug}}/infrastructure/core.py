from example_project.infrastructure.logs import setup_logs
from example_project.infrastructure.sentry import setup_sentry


def setup_infrastructure():
    setup_logs()
    setup_sentry()
