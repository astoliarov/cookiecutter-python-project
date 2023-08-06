from typing import Optional

import structlog
from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse, Response

from {{cookiecutter.project_slug}}.logic.key_value.core import IStorage

logger = structlog.getLogger()


class SetKeyRequest(BaseModel):
    key: str
    value: str
    ttl: Optional[int] = None

    def to_response(self) -> "SetKeyResponse":
        return SetKeyResponse(key=self.key, value=self.value, ttl=self.ttl)


class SetKeyResponse(BaseModel):
    key: str
    value: str
    ttl: Optional[int] = None


class GetKeyResponse(BaseModel):
    key: str
    value: Optional[str] = None


class KeyValueHandler:
    def __init__(self, storage: IStorage) -> None:
        self._storage = storage

    async def set_key(self, request: SetKeyRequest) -> Response:
        response = request.to_response()
        data = response.model_dump()

        logger.info("set_key", request=request)

        await self._storage.set(
            key=request.key,
            value=request.value,
            ttl=request.ttl,
        )

        return JSONResponse(content=data, status_code=200)

    async def get_key(self, key: str) -> Response:
        logger.info("get_key", key=key)

        value = await self._storage.get(
            key=key,
        )

        response = GetKeyResponse(key=key, value=value)

        return JSONResponse(content=response.model_dump(), status_code=200)

    def register_routes(self, router: APIRouter) -> None:
        router.post("/kv", response_model=SetKeyResponse)(self.set_key)
        router.get("/kv", response_model=GetKeyResponse)(self.get_key)

