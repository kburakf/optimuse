import pytest
import json
from unittest.mock import patch
from app.dao.asset_dao import AssetDAO


@pytest.fixture
def sample_file_path(tmp_path):
    data = {"asset": [{"id": 1, "name": "Asset 1"}, {"id": 2, "name": "Asset 2"}]}
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)


@patch("app.dao.asset_dao.find_json_file")
def test_load_assets(mock_find_json, sample_file_path):
    mock_find_json.return_value = sample_file_path
    dao = AssetDAO()
    assets = dao.load_assets()
    assert len(assets) == 2
    assert assets[0].id == 1
    assert assets[0].name == "Asset 1"


@patch("app.dao.asset_dao.find_json_file")
def test_get_asset_by_id(mock_find_json, sample_file_path):
    mock_find_json.return_value = sample_file_path
    dao = AssetDAO()
    asset = dao.get_asset_by_id(1)
    assert asset is not None
    assert asset.id == 1
    assert asset.name == "Asset 1"

    asset = dao.get_asset_by_id(3)
    assert asset is None

    asset = dao.get_asset_by_id(2)
    assert asset is not None
    assert asset.id == 2
    assert asset.name == "Asset 2"


@patch("app.dao.asset_dao.find_json_file")
def test_invalid_file_path(mock_find_json):
    mock_find_json.side_effect = FileNotFoundError("No JSON file found in the specified directory.")
    with pytest.raises(FileNotFoundError):
        AssetDAO()
