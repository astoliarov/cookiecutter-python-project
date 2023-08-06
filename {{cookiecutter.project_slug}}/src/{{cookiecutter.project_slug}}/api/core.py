from fastapi import APIRouter, FastAPI

from {{cookiecutter.project_slug}}.api.handlers.healthcheck import HealthCheckHandler
from {{cookiecutter.project_slug}}.api.handlers.key_value import KeyValueHandler
from {{cookiecutter.project_slug}}.infrastructure.core import setup_infrastructure
from {{cookiecutter.project_slug}}.logic.key_value.in_memory import InMemoryStorage


def build_api() -> FastAPI:
    setup_infrastructure()

    app = FastAPI()

    storage = InMemoryStorage()
    kv_handler = KeyValueHandler(storage)
    healthcheck_handler = HealthCheckHandler()

    sys_router = APIRouter()
    healthcheck_handler.register_routes(sys_router)

    api_v1_router = APIRouter()
    kv_handler.register_routes(api_v1_router)

    app.include_router(api_v1_router, prefix="/api/v1")
    app.include_router(sys_router, prefix="/sys")

    return app

