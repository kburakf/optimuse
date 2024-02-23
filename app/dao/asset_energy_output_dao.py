import json
from typing import Optional
from app.models.asset_energy_output_model import (
    AssetEnergyOutputModel,
)
from app.utils.find_json_file import find_json_file


class AssetEnergyOutputDAO:
    def __init__(self):
        self.file_path = find_json_file()
        self.asset_energy_outputs = self.load_asset_energy_outputs()

    def load_asset_energy_outputs(self) -> list:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return [AssetEnergyOutputModel(**outputs) for outputs in data["asset_energy_output"]]

    def get_energy_output_by_asset_id(self, asset_id: int) -> Optional[AssetEnergyOutputModel]:
        for output in self.asset_energy_outputs:
            if output.asset == asset_id:
                return output
        return None
