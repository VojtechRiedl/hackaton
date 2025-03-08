from sqlalchemy.orm import Session


from ...database import database_manager

def school_zarizeni_by_okres(okres_id: int, db: Session):
    return database_manager.get_schools_zarizeni_by_okres(okres_id, db)
