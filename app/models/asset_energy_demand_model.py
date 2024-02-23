from pydantic import BaseModel


class AssetEnergyDemandModel(BaseModel):
    asset: int
    energy_type: int
    energy_demand: int
