from analyzer import analyze_farm
from recommendations import get_recommendations


def main():
    print("=" * 45)
    print("          🌱 AGRIASSIST")
    print("       SMART FARMING ASSISTANT")
    print("=" * 45)

    print("\nEnter Farm Details\n")

    crop = input("Crop Name          : ")
    soil = input("Soil Type          : ")

    temperature = float(input("Temperature (°C)  : "))
    humidity = float(input("Humidity (%)       : "))
    moisture = float(input("Soil Moisture (%)  : "))
    rainfall = float(input("Rainfall (mm)      : "))

    result = analyze_farm(
        crop,
        soil,
        temperature,
        humidity,
        moisture,
        rainfall
    )

    recommendations = get_recommendations(result)

    print("\n" + "-" * 45)
    print("              ANALYSIS")
    print("-" * 45)

    print(f"\n🌾 Crop              : {result['crop']}")
    print(f"🌱 Crop Health       : {result['health']}")
    print(f"💧 Irrigation Status : {result['irrigation']}")
    print(f"⚠️ Risk Level         : {result['risk']}")

    print("\n💡 Recommendations:")
    for recommendation in recommendations:
        print("  " + recommendation)

    print("\n" + "=" * 45)
    print("       Thank you for using AgriAssist!")
    print("=" * 45)


if __name__ == "__main__":
    main()