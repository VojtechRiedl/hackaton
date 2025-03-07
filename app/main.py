
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.kraje.router import kraje_router
app = FastAPI(
    title="SKIBIDI"
)

cors = {
    "origins": ["*"],
    "methods": ["*"],
    "allowed_headers": ["*"]
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors["origins"],
    allow_methods=cors["methods"],
    allow_headers=cors["allowed_headers"],
)

app.include_router(kraje_router)
