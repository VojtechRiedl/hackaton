from pydantic import BaseModel, Field

class SkolniZarizeni(BaseModel):

    geometry: str = Field(description="Geometrie školního zařízení")