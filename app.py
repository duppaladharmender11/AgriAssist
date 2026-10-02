from flask import Flask, request, jsonify
from flask_cors import CORS

from analyzer import analyze_farm
from recommendations import get_recommendations

app = Flask(__name__)
CORS(app)


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    crop = data["crop"]
    soil = data["soil"]
    temperature = float(data["temperature"])
    humidity = float(data["humidity"])
    moisture = float(data["moisture"])
    rainfall = float(data["rainfall"])

    result = analyze_farm(
        crop,
        soil,
        temperature,
        humidity,
        moisture,
        rainfall
    )

    result["recommendations"] = get_recommendations(result)

    return jsonify(result)


@app.route("/")
def home():
    return jsonify({
        "message": "AgriAssist API is running!"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)