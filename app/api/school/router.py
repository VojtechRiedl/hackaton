from fastapi import APIRouter, Depends

from ...database.database_connection import get_db

from sqlalchemy.orm import Session

from . import school_manager
from ..okresy.schemas import Okres


school_router = APIRouter(prefix="/school", tags=["školy"])


@school_router.get("/{okres_id}")
def get_okres_from_kraj(okres_id: str, db: Session = Depends(get_db)):
    return school_manager.school_zarizeni_by_okres(okres_id, db)


@school_router.get("/red_izo/{red_izo}")
def get_school_by_red_izo(red_izo: int, db: Session = Depends(get_db)):
    return school_manager.school_by_red_izo(red_izo, db)
