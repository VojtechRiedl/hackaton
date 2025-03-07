from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ....database.database_connection import get_db

from .schemas import Okres

from . import kraje_manager

kraje_router = APIRouter(prefix="/kraje", tags=["kraje"])


@kraje_router.get("/{kraj_id}/okresy", response_model=list[Okres])
def get_okresy(kraj_id: str, db: Session = Depends(get_db)):
    kraje_manager.get_okresy_from_kraj(kraj_id, db)

    


