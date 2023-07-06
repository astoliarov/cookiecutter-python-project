import asyncio

import structlog

logger = structlog.get_logger()


class Worker:
    def __init__(self) -> None:
        self._should_stop = False

    def stop(self) -> None:
        self._should_stop = True

    async def execute(self) -> None:
        logger.info("worker started")

        while not self._should_stop:
            logger.info("doing some work")
            await asyncio.sleep(1)

        logger.info("worker finished")
