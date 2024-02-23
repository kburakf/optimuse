from pydantic import BaseModel


class AssetModel(BaseModel):
    id: int
    name: str
