def calculate_merv(particles_removed_03_1, particles_removed_1_3, particles_removed_3_10):
    # Define MERV thresholds as a dictionary
    merv_thresholds = {
        1:  {"0.3-1.0": 0, "1-3": 0, "3-10": 20},
        5:  {"0.3-1.0": 0, "1-3": 0, "3-10": 20},
        6:  {"0.3-1.0": 0, "1-3": 0, "3-10": 35},
        7:  {"0.3-1.0": 0, "1-3": 0, "3-10": 50},
        8:  {"0.3-1.0": 0, "1-3": 20, "3-10": 70},
        9:  {"0.3-1.0": 0, "1-3": 35, "3-10": 75},
        10: {"0.3-1.0": 0, "1-3": 50, "3-10": 80},
        11: {"0.3-1.0": 20, "1-3": 65, "3-10": 85},
        12: {"0.3-1.0": 35, "1-3": 80, "3-10": 90},
        13: {"0.3-1.0": 50, "1-3": 85, "3-10": 90},
        14: {"0.3-1.0": 75, "1-3": 90, "3-10": 95},
        15: {"0.3-1.0": 85, "1-3": 90, "3-10": 95},
        16: {"0.3-1.0": 95, "1-3": 95, "3-10": 95},
    }
    
    # Determine the highest MERV level meeting the criteria
    for merv, thresholds in sorted(merv_thresholds.items()):
        if (particles_removed_03_1 <= thresholds["0.3-1.0"] and
            particles_removed_1_3 <= thresholds["1-3"] and
            particles_removed_3_10 <= thresholds["3-10"]):
            return merv

    return "No suitable MERV level found"

def co_nox_to_pm(co, nox):
    # Example conversion factors (replace with actual data or model)
    a, b = 5, 0.03  # Coefficients for PM_0.3-1
    c, d = 4, 0.02  # Coefficients for PM_1-3
    e, f = 7, 0.04  # Coefficients for PM_3-10

    pm_03_1 = a * co + b * nox
    pm_1_3 = c * co + d * nox
    pm_3_10 = e * co + f * nox

    return pm_03_1, pm_1_3, pm_3_10

def calculate_removal_fraction(predicted_pm_03_1, predicted_pm_1_3, predicted_pm_3_10,  guidlines="EU"):

    if(guidlines == "WHO"):
        safe_pm_03_1 = 5  # Safe threshold for PM2.5 (µg/m³)
        safe_pm_1_3 = 5   # Safe threshold for PM10 (µg/m³)
        safe_pm_3_10 = 15   # Safe threshold for PM10 (µg/m³)
    if(guidlines == "EU"):
        safe_pm_03_1 = 25  # Safe threshold for PM2.5 (µg/m³)
        safe_pm_1_3 = 25   # Safe threshold for PM10 (µg/m³)
        safe_pm_3_10 = 50   # Safe threshold for PM10 (µg/m³)
    # Calculate removal fraction needed
    removal_fraction_03_1 = max(0, (predicted_pm_03_1 - safe_pm_03_1) / predicted_pm_03_1)
    removal_fraction_1_3 = max(0, (predicted_pm_1_3 - safe_pm_1_3) / predicted_pm_1_3)
    removal_fraction_3_10 = max(0, (predicted_pm_3_10 - safe_pm_3_10) / predicted_pm_3_10)
    return removal_fraction_03_1, removal_fraction_1_3, removal_fraction_3_10




def Molecular_to_MERV(co_concentration, nox_concentration, guidlines):
    # Step 1: Convert to PM
    pm_03_1, pm_1_3, pm_3_10 = co_nox_to_pm(co_concentration, nox_concentration)

    # Step 3: Calculate removal fractions
    removal_fraction_03_1, removal_fraction_1_3, removal_fraction_3_10  = calculate_removal_fraction(pm_03_1, pm_1_3, pm_3_10, guidlines)

    # Step 4: Input into MERV function
    merv_level = calculate_merv(removal_fraction_03_1 * 100, removal_fraction_1_3 * 100, removal_fraction_3_10 * 100)
    return merv_level

co_concentration = 6.241646756656867  # Example CO concentration (µg/m³)
nox_concentration = 692.7832307272347  # Example NOx concentration (µg/m³)
merv_level = Molecular_to_MERV(co_concentration, nox_concentration, guidlines="EU")
print(f"The appropriate MERV level is: {merv_level}")
