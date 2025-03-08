from pydantic import BaseModel, Field


class SkolniZarizeni(BaseModel):

    geometry: str = Field(description="Geometrie školního zařízení")


class School(BaseModel):

    lantitude: float | None = Field(
        description="Zeměpisná šířka školního zařízení")
    lontitude: float | None = Field(
        description="Zeměpisná délka školního zařízení")
    head_name: str | None = Field(description="Jméno ředitele")
    head_address: str | None = Field(description="Příjmení ředitele")
    zarizeni: str = Field(description="Název školního zařízení")
    nazev: str | None = Field(description="Název školy")
    obec: str | None = Field(description="Název obce")
    cislo_domovni: int | None = Field(description="Číslo domovní")
    cislo_orientacni: int | None = Field(description="Číslo orientační")
    red_izo: int = Field(description="Číslo IZO školního zařízení")


class SchoolFinance(BaseModel):

    lantitude: float | None = Field(
        description="Zeměpisná šířka školního zařízení")
    lontitude: float | None = Field(
        description="Zeměpisná délka školního zařízení")
    id: int = Field(description="id ")
    ico: int = Field(description="IČO")
    obdobi: int = Field(description="Období")
    dlouhmmaj: float | None = Field(description="Dlouhodobé majetky")
    krpohlbrut: float | None = Field(description="Krátkodobé pohledávky")
    cizzdr: float = Field(description="Číslo zdravotní pojišťovny")
    prijdluh: float = Field(description="Přijaté dluhy")
    kratzav: float = Field(description="Krátkodobé závazky")
    uroky: float = Field(description="Úroky")
    vydaje: float = Field(description="Výdaje")
    pocob: float = Field(description="Počet obyvatel")
    aktiva: float = Field(description="Aktiva")
    saldo: float = Field(description="Saldo")
    naklady: float = Field(description="Náklady")
    dlouzav: float = Field(description="Dlouhodobé závazky")
    vynosy: float = Field(description="Výnosy")
    prijmy: float = Field(description="Příjmy")
    dluhcelk: float = Field(description="Dluh celkem")
    vysledek: float = Field(description="Výsledek")
    uhrdluh: float = Field(description="Uhrazené dluhy")
    pohlbrut: float = Field(description="Pohledávky brutto")
    kratfinmaj: float = Field(description="Krátkodobé finanční majetky")
