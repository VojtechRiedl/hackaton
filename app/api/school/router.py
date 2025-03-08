from fastapi import APIRouter, Depends

from ...database.database_connection import get_db

from sqlalchemy.orm import Session

from . import school_manager


school_router = APIRouter(prefix="/school", tags=["školy"])


@school_router.get("/{okres_id}")
def get_okres_from_kraj(okres_id: str, db: Session = Depends(get_db)):
    return school_manager.school_zarizeni_by_okres(okres_id, db)


@school_router.get("/red_izo/{red_izo}")
def get_school_by_red_izo(red_izo: int, db: Session = Depends(get_db)):
    return school_manager.school_by_red_izo(red_izo, db)


@school_router.get("/finance/{obdobi}")
def get_finance(obdobi: int, db: Session = Depends(get_db)):
    return school_manager.get_finance(obdobi, db)


@school_router.get("/finance/{obdobi}/{red_izo}")
def get_school_finance(obdobi: int, red_izo: int, db: Session = Depends(get_db)):
    return school_manager.get_school_finance(obdobi, red_izo, db)