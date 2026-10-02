import { useState } from "react";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    crop: "",
    soil: "",
    temperature: "",
    humidity: "",
    moisture: "",
    rainfall: "",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const analyzeFarm = async (e) => {
  e.preventDefault();

  try {
    const response = await fetch("https://agriassist-api.vercel.app/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    const data = await response.json();

    setResult(data);
  } catch (error) {
    console.error("Backend connection error:", error);
    alert("Backend server is not running!");
  }
};

  return (
    <div className="app">
      <header>
        <h1>🌱 AgriAssist</h1>
        <p>Smart Farming Decision Support System</p>
      </header>

      <main>
        <section className="card">
          <h2>Farm Details</h2>

          <form onSubmit={analyzeFarm}>
            <input
              name="crop"
              placeholder="Crop Name"
              value={form.crop}
              onChange={handleChange}
              required
            />

            <input
              name="soil"
              placeholder="Soil Type"
              value={form.soil}
              onChange={handleChange}
              required
            />

            <input
              name="temperature"
              type="number"
              placeholder="Temperature (°C)"
              value={form.temperature}
              onChange={handleChange}
              required
            />

            <input
              name="humidity"
              type="number"
              placeholder="Humidity (%)"
              value={form.humidity}
              onChange={handleChange}
              required
            />

            <input
              name="moisture"
              type="number"
              placeholder="Soil Moisture (%)"
              value={form.moisture}
              onChange={handleChange}
              required
            />

            <input
              name="rainfall"
              type="number"
              placeholder="Rainfall (mm)"
              value={form.rainfall}
              onChange={handleChange}
              required
            />

            <button type="submit">🔍 Analyze Farm</button>
          </form>
        </section>

        {result && (
          <section className="card result">
            <h2>📊 Farm Analysis</h2>

            <p>🌾 Crop: <strong>{result.crop}</strong></p>
            <p>🌱 Crop Health: <strong>{result.health}</strong></p>
            <p>💧 Irrigation: <strong>{result.irrigation}</strong></p>
            <p>⚠️ Risk Level: <strong>{result.risk}</strong></p>

            <h3>💡 Recommendations</h3>

            <ul>
              {result.recommendations.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;