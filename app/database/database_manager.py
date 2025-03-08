from sqlalchemy.orm import Session

from ..database import models


def get_okresy_from_kraj(kraj_id: int, db: Session) -> list[models.Okres]:
    okresy = db.query(models.Okres).filter(
        models.Okres.VuscKod == kraj_id).all()
    return okresy


def get_schools_zarizeni_by_okres(okres_id: int, db: Session):

    schools = (
        db.query(models.Mista, models.SchoolZarizeni, models.School)
        .join(models.SchoolStrediska, models.Mista.id == models.SchoolStrediska.adresa)
        .join(models.SchoolZarizeni, models.SchoolStrediska.izo == models.SchoolZarizeni.izo)
        .join(models.School, models.School.ico == models.SchoolZarizeni.ico)
        .filter(models.Mista.okres_id == okres_id)
        .all()
    )

    return schools


def get_school_by_red_izo(izo: int, db: Session):
    return db.query(models.School).filter(models.School.red_izo == izo).first()
