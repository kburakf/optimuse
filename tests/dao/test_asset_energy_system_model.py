import pytest
import json
from unittest.mock import patch
from app.dao.energy_system_dao import EnergySystemDAO


@pytest.fixture
def sample_file_path(tmp_path):
    data = {"energy_system": [{"id": 1, "name": "Electricity"}, {"id": 2, "name": "Gas"}]}
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)


@patch("app.dao.energy_system_dao.find_json_file")
def test_load_energy_systems(mock_find_json, sample_file_path):
    mock_find_json.return_value = sample_file_path
    dao = EnergySystemDAO()
    systems = dao.load_energy_systems()
    assert len(systems) == 2
    assert systems[0].id == 1
    assert systems[0].name == "Electricity"


@patch("app.dao.energy_system_dao.find_json_file")
def test_get_all_energy_systems(mock_find_json, sample_file_path):
    mock_find_json.return_value = sample_file_path
    dao = EnergySystemDAO()
    systems = dao.get_all_energy_systems()
    assert len(systems) == 2
    assert systems[0].id == 1
    assert systems[0].name == "Electricity"
    assert systems[1].id == 2
    assert systems[1].name == "Gas"


@patch("app.dao.energy_system_dao.find_json_file")
def test_invalid_file_path(mock_find_json):
    mock_find_json.side_effect = FileNotFoundError("No JSON file found in the specified directory.")
    with pytest.raises(FileNotFoundError):
        EnergySystemDAO()
