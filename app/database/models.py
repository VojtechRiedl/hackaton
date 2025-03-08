
from .database_connection import Base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Text, Integer, ForeignKey, Double, String, Boolean


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

    red_izo = Column(Integer)
    ico = Column(Integer, primary_key=True)
    nazev = Column(Text, nullable=True)
    ruain = Column(Integer, nullable=True)
    head_name = Column(String, nullable=True)
    head_address = Column(String, nullable=True)
    pocet_studentu = Column(Integer, nullable=True)
    pocet_uceben = Column(Integer, nullable=True)
    pocet_notebook = Column(Integer, nullable=True)
    pocet_pc = Column(Integer, nullable=True)
    wifi = Column(Boolean, nullable=True)

    school_zarizeni = relationship("SchoolZarizeni", back_populates="school")

    finance = relationship("Finance", back_populates="school")


class SchoolZarizeni(Base):
    __tablename__ = "schools_izo"

    izo = Column(Integer, primary_key=True)
    ico = Column(Integer, ForeignKey("schools.ico"), nullable=True)
    nazev = Column(Text, nullable=True)
    kapacita = Column(Integer, nullable=True)

    school = relationship("School", back_populates="school_zarizeni")

    school_strediska = relationship(
        "SchoolStrediska", back_populates="school_zarizeni")


class SchoolStrediska(Base):
    __tablename__ = "schools_strediska"

    id = Column(Integer, primary_key=True)
    izo = Column(Integer, ForeignKey("schools_izo.izo"), nullable=True)
    adresa = Column(Integer, ForeignKey("Mista.id"), nullable=True)

    misto = relationship("Mista", back_populates="school_strediska")

    school_zarizeni = relationship(
        "SchoolZarizeni", back_populates="school_strediska")


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


class Finance(Base):
    __tablename__ = "financni_data"

    id = Column(Integer, primary_key=True)
    ico = Column(Integer, ForeignKey("schools.ico"))
    obdobi = Column(Integer, index=True)
    dlouhmmaj = Column(Double, nullable=True)
    krpohlbrut = Column(Double, nullable=True)
    cizzdr = Column(Double, nullable=True)
    prijdluh = Column(Double, nullable=True)
    kratzav = Column(Double, nullable=True)
    uroky = Column(Double, nullable=True)
    vydaje = Column(Double, nullable=True)
    pocob = Column(Double, nullable=True)
    aktiva = Column(Double, nullable=True)
    saldo = Column(Double, nullable=True)
    naklady = Column(Double, nullable=True)
    dlouzav = Column(Double, nullable=True)
    vynosy = Column(Double, nullable=True)
    prijmy = Column(Double, nullable=True)
    dluhcelk = Column(Double, nullable=True)
    vysledek = Column(Double, nullable=True)
    uhrdluh = Column(Double, nullable=True)
    pohlbrut = Column(Double, nullable=True)
    kratfinmaj = Column(Double, nullable=True)

    school = relationship("School", back_populates="finance")
