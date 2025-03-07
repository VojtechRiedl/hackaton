from pydantic import BaseModel, Field


class Okres(BaseModel):
    gml_id: str | None = Field(description="GML ID")
    Kod: int = Field(description="Kod okresu")
    Nazev: str | None = Field(description="Nazev")
    VuscKod: int = Field(description="Kod kraje")
    geometry: str | None = Field(description="GeoJSON", alias="geometry")