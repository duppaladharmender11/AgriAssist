def analyze_farm(crop, soil, temperature, humidity, moisture, rainfall):

    # Irrigation status
    if moisture < 30:
        irrigation = "REQUIRED"
    elif moisture <= 40:
        irrigation = "MONITOR"
    else:
        irrigation = "NOT REQUIRED"

    # Temperature risk
    if temperature > 35:
        risk = "HIGH"
    elif temperature > 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # Crop health
    if moisture < 20 or temperature > 40:
        health = "POOR"
    elif moisture < 30 or temperature > 35:
        health = "AVERAGE"
    else:
        health = "GOOD"

    return {
        "crop": crop,
        "soil": soil,
        "temperature": temperature,
        "humidity": humidity,
        "moisture": moisture,
        "rainfall": rainfall,
        "irrigation": irrigation,
        "risk": risk,
        "health": health
    }