
from fastapi import FastAPI

from .api.kraje.router import kraje_router
app = FastAPI(
    title="SKIBIDI"
)


app.include_router(kraje_router)