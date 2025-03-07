from pydantic import BaseModel, Field

class Okres(BaseModel):

    gml_id: str = Field(description="GML ID okresu")
    kod: int = Field(description="Kod okresu")
    nazev: str = Field(description="Nazev okresu")
    kraj_id: int = Field(description="ID kraje, ke kteremu okres patri")
    geometry: str = Field(description="Geometrie okresu")

    
