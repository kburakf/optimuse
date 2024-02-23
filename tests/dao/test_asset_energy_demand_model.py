import pytest
from app.models.asset_energy_demand_model import AssetEnergyDemandModel


def test_asset_energy_demand_model():
    asset_id = 1
    energy_type_id = 2
    energy_demand_value = 1000

    asset_energy_demand = AssetEnergyDemandModel(
        asset=asset_id, energy_type=energy_type_id, energy_demand=energy_demand_value
    )

    assert asset_energy_demand.asset == asset_id
    assert asset_energy_demand.energy_type == energy_type_id
    assert asset_energy_demand.energy_demand == energy_demand_value
