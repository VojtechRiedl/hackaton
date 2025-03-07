from sqlalchemy.orm import Session


from ...database import database_manager

from ..okresy.schemas import Okres

def get_okresy_from_kraj(kraj_id: int, db: Session):
    return [Okres(gml_id=okres.gml_id, kod=okres.Kod, nazev=okres.Nazev, kraj_id=okres.VuscKod, geometry=okres.geometry) for okres in database_manager.get_okresy_from_kraj(kraj_id, db)]