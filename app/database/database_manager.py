from sqlalchemy.orm import Session

from ..database import models
from ..api.school.schemas import SkolniZarizeni

def get_okresy_from_kraj(kraj_id: int, db: Session) -> list[models.Okres]:
    okresy = db.query(models.Okres).filter(models.Okres.VuscKod == kraj_id).all()
    return okresy


def get_schools_zarizeni_by_okres(okres_id: int, db: Session):

    schools = (
        db.query(models.Address)
        .join(models.SchoolStrediska, models.Address.Kod == models.SchoolStrediska.adresa)
        .join(models.StavebniObjekt, models.StavebniObjekt.Kod == models.Address.StavebniObjektKod, isouter=True)
        .join(models.CastObce, models.CastObce.Kod == models.StavebniObjekt.CastObceKod,  isouter=True)
        .join(models.Obec, models.Obec.Kod == models.CastObce.ObecKod, isouter=True)
        .filter(models.Obec.OkresKod == okres_id)
    )

    print(schools)
    return schools.all()