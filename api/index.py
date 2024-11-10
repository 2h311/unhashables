from pathlib import Path
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from hasher import route_bcrypt
from webapp import route_index


def include_router(app):
    app.include_router(route_bcrypt.router, prefix="", tags=["API"])
    app.include_router(route_index.router, prefix="", tags=["Index Page"])


def mount_static(app):
    app.mount(
        "/static", StaticFiles(directory=Path("api", "webapp", "static")), name="static"
    )


def start_app():
    app = FastAPI(title="bcrypt-generator", version="1.0.0")
    include_router(app)
    mount_static(app)
    return app


app = start_app()
