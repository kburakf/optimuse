from pydantic import BaseModel


class AssetEnergySystemModel(BaseModel):
    asset: int
    energy_system: int
    energy_type: int
