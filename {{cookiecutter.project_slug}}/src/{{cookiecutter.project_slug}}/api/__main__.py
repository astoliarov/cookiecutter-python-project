from typing import Any

import uvicorn

from {{cookiecutter.project_slug}}.api.core import build_api
from {{cookiecutter.project_slug}}.api.settings import ApiSettings

web_app = None

api_settings = ApiSettings()


def uvicorn_factory() -> Any:
    async def app(scope: Any, receive: Any, send: Any) -> Any:
        global web_app
        if web_app is None:
            web_app = build_api()

        return await web_app(scope, receive, send)

    return app


if __name__ == "__main__":
    uvicorn.run(
        "{{cookiecutter.project_slug}}.api.__main__:uvicorn_factory",
        factory=True,
        reload=api_settings.reload,
        access_log=api_settings.access_log,
        port=api_settings.port,
        host=api_settings.host,
        workers=api_settings.workers,
    )
