from pydantic import BaseModel


class EnergySystemModel(BaseModel):
    id: int
    name: str
