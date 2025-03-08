from sqlalchemy.orm import Session


from ...database import database_manager

def school_zarizeni_by_okres(okres_id: int, db: Session):

    return [{
        "lan": a.lantitude,
        "lon": a.lontitude,
        "zarizeni": b.nazev, 
        "nazev": c.nazev,
    } for a, b, c in database_manager.get_schools_zarizeni_by_okres(okres_id, db)]


    return database_manager.get_schools_zarizeni_by_okres(okres_id, db)
