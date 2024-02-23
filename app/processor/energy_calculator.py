def calculate_energy_demand(
    asset,
    asset_energy_output,
    asset_energy_systems,
    asset_energy_demands,
    energy_types,
    energy_systems,
):
    # Identify the electricity system ID
    electricity_system_id = next(
        (system.id for system in energy_systems if system.name.lower() == "electricity"), None
    )

    # Initialize storage for the calculated demands
    energy_demands = {etype.name: 0 for etype in energy_types}
    total_initial_demand = 0  # Total demand before any reductions

    # Process each energy demand
    for demand in asset_energy_demands:
        energy_type = next(
            (etype for etype in energy_types if etype.id == demand.energy_type), None
        )

        if energy_type:
            system_id = next(
                (
                    aes.energy_system
                    for aes in asset_energy_systems
                    if aes.energy_type == demand.energy_type
                ),
                None,
            )

            # Initial total demand (before reduction)
            total_initial_demand += demand.energy_demand

            # Adjust demand if the system is electricity
            if system_id == electricity_system_id:
                reduced_demand = max(demand.energy_demand - asset_energy_output.energy_output, 0)
            else:
                reduced_demand = demand.energy_demand

            energy_demands[energy_type.name] += reduced_demand

    # Calculate the total reduced demand
    total_energy_demand_after_reduction = sum(energy_demands.values())

    # Calculate the energy output reduction percentage
    if total_initial_demand > 0:
        energy_output_reduction = round(
            100 - ((total_energy_demand_after_reduction / total_initial_demand) * 100), 2
        )
    else:
        energy_output_reduction = 0

    return {
        "name": asset.name,
        "energy_types": energy_demands,
        "total_energy_demand": total_energy_demand_after_reduction,
        "energy_output_reduction": energy_output_reduction,
    }
