import pytest
from app.models.energy_type_model import EnergyTypeModel


def test_energy_type_model():
    energy_type = EnergyTypeModel(id=1, name="Electricity")

    assert energy_type.id == 1
    assert energy_type.name == "Electricity"
