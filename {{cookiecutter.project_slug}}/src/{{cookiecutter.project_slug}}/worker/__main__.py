import asyncio
import functools
import signal

import structlog

from {{cookiecutter.project_slug}}.logs import setup_logs
from {{cookiecutter.project_slug}}.worker.worker import Worker

logger = structlog.get_logger()


def shutdown(_signal, worker):
    logger.info("Received signal. Sending signal to stop worker...", signal=_signal)
    worker.stop()


if __name__ == "__main__":
    setup_logs()

    worker = Worker()

    loop = asyncio.get_event_loop()

    signals = (signal.SIGTERM, signal.SIGINT)
    for _signal in signals:
        loop.add_signal_handler(_signal, lambda: shutdown(_signal, worker))

    logger.info("starting worker")

    try:
        loop.run_until_complete(worker.execute())
    finally:
        loop.close()
        logger.info("worker stopped")
