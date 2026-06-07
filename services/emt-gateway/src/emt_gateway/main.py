from fastapi import FastAPI
from emt_gateway.config import settings
from emt_gateway.api.v1.routes.buses import router as buses_router

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    debug = settings.debug,
)

app.include_router(buses_router, prefix = "/api/v1")

@app.get("/health")
async def health():
    return {"status": "ok",
            "service": settings.app_name
            }