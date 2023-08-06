from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse, Response

# Useful links:
# https://medium.com/@AADota/kubernetes-liveness-and-readiness-probes-difference-1b659c369e17
# https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
# https://www.fairwinds.com/blog/a-guide-to-understanding-kubernetes-liveness-probes-best-practices


class HealthCheckHandler:
    async def liveness_probe(self) -> Response:
        return JSONResponse(content={}, status_code=HTTPStatus.OK)

    async def readiness_probe(self) -> Response:
        return JSONResponse(content={}, status_code=HTTPStatus.OK)

    def register_routes(self, router: APIRouter) -> None:
        router.get("/liveness_probe")(self.liveness_probe)
        router.get("/readiness_probe")(self.readiness_probe)
        router.get("/health")(self.liveness_probe)
