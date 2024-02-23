import json
from typing import Optional
from app.utils.find_json_file import find_json_file

from app.models.asset_model import AssetModel


class AssetDAO:
    def __init__(self):
        self.file_path = find_json_file()
        self.assets = self.load_assets()

    def load_assets(self) -> list:
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return [AssetModel(**asset) for asset in data["asset"]]

    def get_asset_by_id(self, asset_id: int) -> Optional[AssetModel]:
        for asset in self.assets:
            if asset.id == asset_id:
                return asset
        return None
