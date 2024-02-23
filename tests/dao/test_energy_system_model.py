import pytest
from app.models.energy_system_model import EnergySystemModel


def test_energy_system_model():
    energy_system = EnergySystemModel(id=1, name="Electricity")

    assert energy_system.id == 1
    assert energy_system.name == "Electricity"
