
from .database_connection import Base

from sqlalchemy import Column, Text, Integer


class Okres(Base):
    __tablename__ = "Okresy"

    gml_id = Column(Text, primary_key=True)
    Kod = Column(Integer, nullable=True)
    Nazev = Column(Text, nullable=True)
    VuscKod = Column(Integer, nullable=True)
    geometry = Column(Text, nullable=True)


class kraj(Base):
    __tablename__ = "kraje"

    gml_id = Column(Text, primary_key=True)
    Kod = Column(Integer, nullable=True)
    Nazev = Column(Text, nullable=True)
    geometry = Column(Text, nullable=True)
