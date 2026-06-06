from fastapi import FastAPI
from emt_gateway.config import settings

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    debug = settings.debug,
)

@app.get("/health")
async def health():
    return {"status": "ok",
            "service": settings.app_name
            }