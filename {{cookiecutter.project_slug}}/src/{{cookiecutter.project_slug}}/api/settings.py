from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    port: int = 8080
    host: str = "0.0.0.0"
    workers: int = 2
    reload: bool = False
    access_log: bool = True

    class Config:
        allow_mutation = False
        env_prefix = "API_"
