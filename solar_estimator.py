
import numpy as np

def estimate_solar_potential(mask):
    pixel_area = 0.25  # Assume each pixel is 0.5m x 0.5m
    usable_pixels = np.sum(mask[:, :, 0] > 100)  # Assuming white rooftop mask
    usable_area = usable_pixels * pixel_area

    panel_efficiency = 0.18  # 18%
    solar_irradiance = 5.5  # kWh/m²/day
    days_per_year = 365

    system_size_kw = usable_area * panel_efficiency
    annual_output_kwh = system_size_kw * solar_irradiance * days_per_year
    estimated_cost = system_size_kw * 60000  # ₹60,000 per kW
    annual_savings = annual_output_kwh * 7  # ₹7/kWh
    roi_years = estimated_cost / annual_savings

    return {
        "usable_area": usable_area,
        "system_size_kw": system_size_kw,
        "annual_output_kwh": annual_output_kwh,
        "roi_years": roi_years
    }
