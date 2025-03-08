
from .database_connection import Base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Text, Integer, ForeignKey, Double, String


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

class School(Base):
    __tablename__ = "schools"   

    ico = Column(Integer, primary_key=True)
    nazev = Column(Text, nullable=True)


    school_zarizeni = relationship("SchoolZarizeni", back_populates="school")

class SchoolZarizeni(Base):
    __tablename__ = "schools_izo"

    izo = Column(Integer, primary_key=True)
    ico = Column(Integer, ForeignKey("schools.ico"), nullable=True)
    nazev = Column(Text, nullable=True)
    kapacita = Column(Integer, nullable=True)

    school = relationship("School", back_populates="school_zarizeni")

    school_strediska = relationship("SchoolStrediska", back_populates="school_zarizeni")

class SchoolStrediska(Base):
    __tablename__ = "schools_strediska"

    id = Column(Integer, primary_key=True)
    izo = Column(Integer, ForeignKey("schools_izo.izo"), nullable=True)
    adresa = Column(Integer, ForeignKey("Mista.id"), nullable=True)

    misto = relationship("Mista", back_populates="school_strediska")

    school_zarizeni = relationship("SchoolZarizeni", back_populates="school_strediska")

class Mista(Base):
    __tablename__ = "Mista"

    id = Column(Integer, primary_key=True)
    cislo_domovni = Column(Integer, nullable=True)
    cislo_orientacni = Column(Integer, nullable=True)
    psc = Column(Integer, nullable=True)
    lontitude = Column(Double, nullable=True)
    lantitude = Column(Double, nullable=True)
    okres_id = Column(Integer, nullable=True)
    kraj_id = Column(Integer, nullable=True)
    obec = Column(String, nullable=True)
    
    school_strediska = relationship("SchoolStrediska", back_populates="misto")
