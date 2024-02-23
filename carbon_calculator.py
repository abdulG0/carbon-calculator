import time  # We'll use this for tracking execution time

def calculate_carbon_footprint(device_type, usage_hours, region="average"):
    """
    Calculates an estimated carbon footprint based on device type, usage, and region.

    Args:
        device_type (str): Type of device (e.g., "laptop", "desktop", "server")
        usage_hours (float): Hours of usage per day
        region (str, optional): Region for carbon intensity. Defaults to "average".

    Returns:
        float: Estimated carbon emissions in grams of CO2e
    """

    # Estimated power consumption in watts (you'll need to refine these)
    device_power = {
        "laptop": 50,
        "desktop": 100,
        "server": 500
    }

    # Regional carbon intensity (grams CO2e per kilowatt-hour)
    # Source: https://www.electricitymap.org/map (these change in real-time)
    carbon_intensity = {
        "average": 500,  # Placeholder - world average
        "south_africa": 850,
        "france": 80
    }

    watts_used = device_power.get(device_type, 100)  # Default to 100 if not found
    kilowatt_hours_daily = (watts_used * usage_hours) / 1000
    co2e_grams_daily = kilowatt_hours_daily * carbon_intensity.get(region, 500)

    return co2e_grams_daily

if __name__ == "__main__":
    start_time = time.time()

    device = input("Enter device type (laptop, desktop, server): ")
    hours = float(input("Enter daily usage hours: "))
    region = input("Enter your region (or leave blank for average): ")

    emissions = calculate_carbon_footprint(device, hours, region)

    print(f"Estimated daily carbon emissions: {emissions:.2f} grams of CO2e")

    end_time = time.time()
    print(f"Calculation took: {end_time - start_time:.4f} seconds")
