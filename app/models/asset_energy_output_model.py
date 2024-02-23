from pydantic import BaseModel


class AssetEnergyOutputModel(BaseModel):
    asset: int
    energy_output: int
