from fastapi import APIRouter, HTTPException

from app.dao.asset_dao import AssetDAO
from app.dao.asset_energy_demand_dao import AssetEnergyDemandDAO
from app.dao.asset_energy_output_dao import AssetEnergyOutputDAO
from app.dao.energy_system_dao import EnergySystemDAO
from app.dao.energy_type_dao import EnergyTypeDAO
from app.dao.asset_energy_system_dao import AssetEnergySystemDAO
from app.processor import energy_calculator

router = APIRouter()

asset_dao = AssetDAO()
energy_demand_dao = AssetEnergyDemandDAO()
energy_output_dao = AssetEnergyOutputDAO()
asset_energy_system_dao = AssetEnergySystemDAO()
energy_type_dao = EnergyTypeDAO()
energy_system_dao = EnergySystemDAO()


@router.get("/{asset_id}")
def get_asset_details(asset_id: int):
    asset = asset_dao.get_asset_by_id(asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    asset_energy_demands = energy_demand_dao.get_energy_demands_by_asset_id(asset_id)

    if len(asset_energy_demands) == 0:
        raise HTTPException(status_code=404, detail="Asset energy demands not found")

    asset_energy_output = energy_output_dao.get_energy_output_by_asset_id(asset_id)

    if not asset_energy_output:
        raise HTTPException(status_code=404, detail="Asset energy output not found")

    asset_energy_systems = asset_energy_system_dao.get_energy_systems_by_asset_id(asset_id)

    if len(asset_energy_systems) == 0:
        raise HTTPException(status_code=404, detail="Asset energy system not found")

    energy_types = energy_type_dao.get_all_energy_types()

    if len(energy_types) == 0:
        raise HTTPException(status_code=404, detail="Energy types not found")

    energy_systems = energy_system_dao.get_all_energy_systems()

    if len(energy_systems) == 0:
        raise HTTPException(status_code=404, detail="Energy systems not found")

    return energy_calculator.calculate_energy_demand(
        asset,
        asset_energy_output,
        asset_energy_systems,
        asset_energy_demands,
        energy_types,
        energy_systems,
    )
