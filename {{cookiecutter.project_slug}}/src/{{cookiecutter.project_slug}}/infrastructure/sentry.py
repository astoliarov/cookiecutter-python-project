from typing import Optional

import sentry_sdk
import structlog
from pydantic import BaseSettings

logger = structlog.getLogger()


class SentrySettings(BaseSettings):
    dsn: Optional[str] = None

    class Config:
        allow_mutation = False
        env_prefix = "SENTRY_"


def setup_sentry() -> None:
    settings = SentrySettings()

    if not settings.dsn:
        logger.debug("no sentry DSN. Skip sentry initialization")
        return

    sentry_sdk.init(settings.dsn)
    logger.debug("sentry initialized")
