import json
from app.models.energy_system_model import EnergySystemModel
from app.utils.find_json_file import find_json_file


class EnergySystemDAO:
    def __init__(self):
        self.file_path = find_json_file()
        self.energy_systems = self.load_energy_systems()

    def load_energy_systems(self) -> list:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return [EnergySystemModel(**energy_systems) for energy_systems in data["energy_system"]]

    def get_all_energy_systems(self) -> list[EnergySystemModel]:
        return self.energy_systems
