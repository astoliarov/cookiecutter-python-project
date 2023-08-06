from typing import Optional

import sentry_sdk
import structlog
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = structlog.getLogger()


class SentrySettings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True, env_prefix="SENTRY_")

    dsn: Optional[str] = None


def setup_sentry() -> None:
    settings = SentrySettings()

    if not settings.dsn:
        logger.debug("no sentry DSN. Skip sentry initialization")
        return

    sentry_sdk.init(settings.dsn)
    logger.debug("sentry initialized")
