
from fastapi import FastAPI

from .api.kraje.router import kraje_router
from .api.school.router import school_router
app = FastAPI(
    title="SKIBIDI"
)


app.include_router(kraje_router)
app.include_router(school_router)