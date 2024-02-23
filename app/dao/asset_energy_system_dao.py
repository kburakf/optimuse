import json
from typing import List
from app.models.asset_energy_system_model import (
    AssetEnergySystemModel,
)
from app.utils.find_json_file import find_json_file


class AssetEnergySystemDAO:
    def __init__(self):
        self.file_path = find_json_file()
        self.asset_energy_systems = self.load_asset_energy_systems()

    def load_asset_energy_systems(self) -> List[AssetEnergySystemModel]:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return [AssetEnergySystemModel(**systems) for systems in data["asset_energy_system"]]

    def get_energy_systems_by_asset_id(self, asset_id: int) -> List[AssetEnergySystemModel]:
        return [system for system in self.asset_energy_systems if system.asset == asset_id]
