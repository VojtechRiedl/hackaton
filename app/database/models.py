
from .database_connection import Base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Text, Integer, ForeignKey


class Okres(Base):
    __tablename__ = "Okresy"

    gml_id = Column(Text, primary_key=True)
    Kod = Column(Integer, nullable=True)
    Nazev = Column(Text, nullable=True)
    VuscKod = Column(Integer, nullable=True)
    geometry = Column(Text, nullable=True)

    obec = relationship("Obec", back_populates="okres")

class kraj(Base):
    __tablename__ = "kraje"

    gml_id = Column(Text, primary_key=True)
    Kod = Column(Integer, nullable=True)
    Nazev = Column(Text, nullable=True)
    geometry = Column(Text, nullable=True)


class Obec(Base):
    __tablename__ = "Obce"

    Kod = Column(Integer, primary_key=True)
    Nazev = Column(Text, nullable=True)
    geometry = Column(Text, nullable=True)
    OkresKod = Column(Integer, ForeignKey("Okresy.Kod"), nullable=True)

    okres = relationship("Okres", back_populates="obec")

    cast_obce = relationship("CastObce", back_populates="obec")

class CastObce(Base):
    __tablename__ = "CastiObci"

    Kod = Column(Integer, primary_key=True)
    Nazev = Column(Text, nullable=True)
    geometry = Column(Text, nullable=True)
    ObecKod = Column(Integer, ForeignKey("Obce.Kod"), nullable=True)

    obec = relationship("Obec", back_populates="cast_obce")

    stavebni_objekty = relationship("StavebniObjekt", back_populates="cast_obce")

class School(Base):
    __tablename__ = "schools"   

    ico = Column(Integer, primary_key=True)
    nazev = Column(Text, nullable=True)


    school_zarizeni = relationship("SchoolZarizeni", back_populates="school")

class SchoolZarizeni(Base):
    __tablename__ = "school_izo"

    izo = Column(Integer, primary_key=True)
    ico = Column(Integer, ForeignKey("schools.ico"), nullable=True)
    nazev = Column(Text, nullable=True)
    kapacita = Column(Integer, nullable=True)

    school = relationship("School", back_populates="school_zarizeni")

    school_strediska = relationship("SchoolStrediska", back_populates="school_zarizeni")

class SchoolStrediska(Base):
    __tablename__ = "schools_strediska"

    id = Column(Integer, primary_key=True)
    izo = Column(Integer, ForeignKey("school_izo.izo"), nullable=True)
    adresa = Column(Integer, ForeignKey("AdresniMista.Kod"), nullable=True)

    address = relationship("Address", back_populates="school_strediska")

    school_zarizeni = relationship("SchoolZarizeni", back_populates="school_strediska")


class Address(Base):
    __tablename__ = "AdresniMista"

    Kod = Column(Integer, primary_key=True)
    geometry = Column(Text, nullable=True)
    StavebniObjektKod = Column(Integer, ForeignKey("StavebniObjekty.Kod"), nullable=True)

    stavebni_objekty = relationship("StavebniObjekt", back_populates="address")

    school_strediska = relationship("SchoolStrediska", back_populates="address")

    

class StavebniObjekt(Base):
    __tablename__ = "StavebniObjekty"

    Kod = Column(Integer, primary_key=True)
    Nazev = Column(Text, nullable=True)
    geometry = Column(Text, nullable=True)
    CastObceKod = Column(Integer, ForeignKey("CastiObci.Kod"), nullable=True)

    cast_obce = relationship("CastObce", back_populates="stavebni_objekty")

    address = relationship("Address", back_populates="stavebni_objekty")

