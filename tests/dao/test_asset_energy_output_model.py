import pytest
import json
from unittest.mock import patch
from app.dao.asset_energy_output_dao import AssetEnergyOutputDAO


@pytest.fixture
def sample_file_path(tmp_path):
    data = {
        "asset_energy_output": [
            {"asset": 1, "energy_output": 100},
            {"asset": 2, "energy_output": 200},
        ]
    }
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)


@patch("app.dao.asset_energy_output_dao.find_json_file")
def test_load_asset_energy_outputs(mock_find_json, sample_file_path):
    mock_find_json.return_value = sample_file_path
    dao = AssetEnergyOutputDAO()
    outputs = dao.load_asset_energy_outputs()
    assert len(outputs) == 2
    assert outputs[0].asset == 1
    assert outputs[0].energy_output == 100


@patch("app.dao.asset_energy_output_dao.find_json_file")
def test_get_energy_output_by_asset_id(mock_find_json, sample_file_path):
    mock_find_json.return_value = sample_file_path
    dao = AssetEnergyOutputDAO()
    output = dao.get_energy_output_by_asset_id(1)
    assert output is not None
    assert output.asset == 1
    assert output.energy_output == 100

    output = dao.get_energy_output_by_asset_id(3)
    assert output is None

    output = dao.get_energy_output_by_asset_id(2)
    assert output is not None
    assert output.asset == 2
    assert output.energy_output == 200


@patch("app.dao.asset_energy_output_dao.find_json_file")
def test_invalid_file_path(mock_find_json):
    mock_find_json.side_effect = FileNotFoundError("No JSON file found in the specified directory.")
    with pytest.raises(FileNotFoundError):
        AssetEnergyOutputDAO()
