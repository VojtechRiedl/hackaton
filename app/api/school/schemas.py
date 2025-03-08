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
