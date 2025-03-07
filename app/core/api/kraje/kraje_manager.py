
from .schemas import Okres
from sqlalchemy.orm import Session

from ....database import database_manager

def get_okresy_from_kraj(kraj_id: str, db: Session) -> list[Okres]:
    return [Okres(**okres.__dict__) for okres in database_manager.get_okresy_from_kraj(kraj_id, db)]