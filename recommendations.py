def get_recommendations(data):
    recommendations = []

    if data["irrigation"] == "REQUIRED":
        recommendations.append("💧 Irrigation is recommended. Soil moisture is low.")

    elif data["irrigation"] == "MONITOR":
        recommendations.append("💧 Monitor soil moisture regularly.")

    else:
        recommendations.append("💧 Irrigation is not required now.")

    if data["risk"] == "HIGH":
        recommendations.append("⚠️ High heat risk. Provide adequate water and monitor the crop.")

    elif data["risk"] == "MEDIUM":
        recommendations.append("⚠️ Moderate temperature risk. Monitor the crop.")

    if data["health"] == "GOOD":
        recommendations.append("🌱 Crop condition looks good.")

    elif data["health"] == "AVERAGE":
        recommendations.append("🌱 Crop needs regular monitoring.")

    else:
        recommendations.append("🚨 Crop needs immediate attention.")

    if data["rainfall"] > 100:
        recommendations.append("🌧️ Rainfall is high. Avoid unnecessary irrigation.")

    return recommendations