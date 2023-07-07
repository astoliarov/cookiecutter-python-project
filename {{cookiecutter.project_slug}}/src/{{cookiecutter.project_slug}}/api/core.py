from fastapi import APIRouter, FastAPI

from {{cookiecutter.project_slug}}.api.handlers.key_value import KeyValueHandler
from {{cookiecutter.project_slug}}.infrastructure.core import setup_infrastructure
from {{cookiecutter.project_slug}}.logic.key_value.in_memory import InMemoryStorage


def build_api() -> FastAPI:
    setup_infrastructure()

    app = FastAPI()

    storage = InMemoryStorage()
    handler = KeyValueHandler(storage)

    api_v1_router = APIRouter()
    handler.register_routes(api_v1_router)

    app.include_router(api_v1_router, prefix="/api/v1")

    return app
