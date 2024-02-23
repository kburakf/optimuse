import pytest
from app.processor.energy_calculator import calculate_energy_demand


def test_calculate_energy_demand(
    asset_fixture,
    asset_energy_output_fixture,
    asset_energy_systems_fixture,
    asset_energy_demands_fixture,
    energy_types_fixture,
    energy_systems_fixture,
):
    # Mocked data representing what your DAOs would return
    asset = asset_fixture
    asset_energy_output = asset_energy_output_fixture
    asset_energy_systems = asset_energy_systems_fixture
    asset_energy_demands = asset_energy_demands_fixture
    energy_types = energy_types_fixture
    energy_systems = energy_systems_fixture

    expected_result = {
        "name": "High Rise",
        "energy_types": {
            "heat": 853452,
            "water": 724213,
            "light": 438889,
            "cool": 536702,
        },
        "total_energy_demand": 2553256,
        "energy_output_reduction": 8.29,
    }

    # Call the function with the mocked data
    result = calculate_energy_demand(
        asset,
        asset_energy_output,
        asset_energy_systems,
        asset_energy_demands,
        energy_types,
        energy_systems,
    )

    assert result == expected_result
