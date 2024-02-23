from starlette.middleware.gzip import GZipMiddleware
from fastapi import FastAPI
from app import routers


app = FastAPI(title="FastAPI", version="0.0.1")
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(routers.asset_router.router, prefix="/api/assets", tags=["API_ASSETS"])
