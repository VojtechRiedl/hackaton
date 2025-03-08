from sqlalchemy.orm import Session


from ...database import database_manager

from .schemas import School


def school_zarizeni_by_okres(okres_id: int, db: Session):

    return [School(
        lantitude=a.lantitude,
        lontitude=a.lontitude,
        zarizeni=b.nazev,
        nazev=c.nazev,
        obec=a.obec,
        cislo_orientacni=a.cislo_orientacni,
        cislo_domovni=a.cislo_domovni
    ) for a, b, c in database_manager.get_schools_zarizeni_by_okres(okres_id, db)]


def school_by_red_izo(izo: int, db: Session):
    return database_manager.get_school_by_red_izo(izo, db)
