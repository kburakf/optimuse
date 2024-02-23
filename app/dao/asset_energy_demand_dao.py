import json
from typing import List
from app.utils.find_json_file import find_json_file
from app.models.asset_energy_demand_model import AssetEnergyDemandModel


class AssetEnergyDemandDAO:
    def __init__(self):
        self.file_path = find_json_file()
        self.asset_energy_demand = self.load_asset_energy_demands()

    def load_asset_energy_demands(self) -> List[AssetEnergyDemandModel]:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return [AssetEnergyDemandModel(**demands) for demands in data["asset_energy_demand"]]

    def get_energy_demands_by_asset_id(self, asset_id: int) -> List[AssetEnergyDemandModel]:
        return [demand for demand in self.asset_energy_demand if demand.asset == asset_id]
