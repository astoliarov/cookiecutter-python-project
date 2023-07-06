from fastapi import APIRouter, FastAPI

from {{cookiecutter.project_slug}}.api.handlers.key_value import KeyValueHandler
from {{cookiecutter.project_slug}}.logic.key_value.in_memory import InMemoryStorage
from {{cookiecutter.project_slug}}.logs import setup_logs


def build_api() -> FastAPI:
    setup_logs()

    app = FastAPI()

    storage = InMemoryStorage()
    handler = KeyValueHandler(storage)

    api_v1_router = APIRouter()
    handler.register_routes(api_v1_router)

    app.include_router(api_v1_router, prefix="/api/v1")

    return app
