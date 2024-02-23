from pydantic import BaseModel


class EnergyTypeModel(BaseModel):
    id: int
    name: str
