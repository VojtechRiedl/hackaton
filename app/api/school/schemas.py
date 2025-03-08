from pydantic import BaseModel, Field

class SkolniZarizeni(BaseModel):

    geometry: str = Field(description="Geometrie školního zařízení")



class School(BaseModel):

    lantitude: float | None = Field(description="Zeměpisná šířka školního zařízení")
    lontitude: float | None  = Field(description="Zeměpisná délka školního zařízení")
    zarizeni: str = Field(description="Název školního zařízení")
    nazev: str | None = Field(description="Název školy")
    obec: str | None = Field(description="Název obce")
    cislo_domovni: int | None = Field(description="Číslo domovní")
    cislo_orientacni: int | None = Field(description="Číslo orientační")
    red_izo: int = Field(description="Číslo IZO školního zařízení")

class SchoolFinance(BaseModel):

    lantitude: float | None = Field(description="Zeměpisná šířka školního zařízení")
    lontitude: float | None = Field(description="Zeměpisná délka školního zařízení")
    id: int = Field(description="id ")
    ico: int = Field(description="IČO")
    obdobi: int = Field(description="Období")
    dlouhmmaj: int | None = Field(description="Dlouhodobé majetky")
    krpohlbrut: int | None = Field(description="Krátkodobé pohledávky")
    cizzdr: int = Field(description="Číslo zdravotní pojišťovny")
    prijdluh: int = Field(description="Přijaté dluhy")
    kratzav: int = Field(description="Krátkodobé závazky")
    uroky: int = Field(description="Úroky")
    vydaje: int = Field(description="Výdaje")
    pocob: int = Field(description="Počet obyvatel")
    aktiva: int = Field(description="Aktiva")
    saldo: int = Field(description="Saldo")
    naklady: int =   Field(description="Náklady")
    dlouzav: int  = Field(description="Dlouhodobé závazky")
    vynosy: int = Field(description="Výnosy")
    prijmy: int = Field(description="Příjmy")
    dluhcelk: int = Field(description="Dluh celkem")
    vysledek: int = Field(description="Výsledek")
    uhrdluh: int = Field(description="Uhrazené dluhy")
    pohlbrut: int = Field(description="Pohledávky brutto")
    kratfinmaj: int = Field(description="Krátkodobé finanční majetky")
