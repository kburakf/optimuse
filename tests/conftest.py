import pytest
from app.models.asset_model import AssetModel
from app.models.asset_energy_demand_model import AssetEnergyDemandModel
from app.models.asset_energy_output_model import AssetEnergyOutputModel
from app.models.asset_energy_system_model import AssetEnergySystemModel
from app.models.energy_system_model import EnergySystemModel
from app.models.energy_type_model import EnergyTypeModel


@pytest.fixture
def asset_fixture():
    return AssetModel(id=1, name="High Rise")


@pytest.fixture
def asset_energy_output_fixture():
    return AssetEnergyOutputModel(asset=1, energy_output=115432)


@pytest.fixture
def asset_energy_systems_fixture():
    return [
        AssetEnergySystemModel(asset=1, energy_system=2, energy_type=1),
        AssetEnergySystemModel(asset=1, energy_system=3, energy_type=2),
        AssetEnergySystemModel(asset=1, energy_system=1, energy_type=3),
        AssetEnergySystemModel(asset=1, energy_system=1, energy_type=4),
    ]


@pytest.fixture
def asset_energy_demands_fixture():
    return [
        AssetEnergyDemandModel(asset=1, energy_type=1, energy_demand=853452),
        AssetEnergyDemandModel(asset=1, energy_type=2, energy_demand=724213),
        AssetEnergyDemandModel(asset=1, energy_type=3, energy_demand=554321),
        AssetEnergyDemandModel(asset=1, energy_type=4, energy_demand=652134),
    ]


@pytest.fixture
def energy_types_fixture():
    return [
        EnergyTypeModel(id=1, name="heat"),
        EnergyTypeModel(id=2, name="water"),
        EnergyTypeModel(id=3, name="light"),
        EnergyTypeModel(id=4, name="cool"),
    ]


@pytest.fixture
def energy_systems_fixture():
    return [
        EnergySystemModel(id=1, name="electricity"),
        EnergySystemModel(id=2, name="district_heating"),
        EnergySystemModel(id=3, name="coal"),
    ]
