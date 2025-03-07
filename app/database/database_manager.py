from sqlalchemy.orm import Session

from ..database.models import Okres

def get_okresy_from_kraj(kraj_id: str, db: Session) -> list[Okres]:
    okresy = db.query(Okres).filter(Okres.VuscKod == kraj_id).all()
    return okresy