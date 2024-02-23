import json
from app.models.energy_type_model import EnergyTypeModel
from app.utils.find_json_file import find_json_file


class EnergyTypeDAO:
    def __init__(self):
        self.file_path = find_json_file()
        self.energy_types = self.load_energy_types()

    def load_energy_types(self) -> list:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return [EnergyTypeModel(**energy_types) for energy_types in data["energy_type"]]

    def get_all_energy_types(self) -> list[EnergyTypeModel]:
        return self.energy_types
