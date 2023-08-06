from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(frozen=True, env_prefix="API_")

    port: int = 8080
    host: str = "0.0.0.0"
    workers: int = 2
    reload: bool = False
    access_log: bool = True
