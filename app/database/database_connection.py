from ..core.settings import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(settings.database.to_sqlalchemy_url())

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()