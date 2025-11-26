import json
import os
import pandas as pd

def clean_weather_data():
    # Ensure the folder exists
    os.makedirs("data_clean", exist_ok=True)

    # Get the latest file from data_raw
    raw_path = "data_raw"
    files = sorted(
        [f for f in os.listdir(raw_path) if f.endswith(".json")],
        reverse=True
    )

    if not files:
        print("[ERROR] No raw data found. Run fetch_data.py first.")
        return

    latest_file = os.path.join(raw_path, files[0])

    # Load the JSON data
    with open(latest_file, "r") as f:
        data = json.load(f)

    # Extract useful fields safely
    cleaned = {
        "city": data.get("name"),
        "temp": data["main"].get("temp"),
        "feels_like": data["main"].get("feels_like"),
        "humidity": data["main"].get("humidity"),
        "pressure": data["main"].get("pressure"),
        "wind_speed": data["wind"].get("speed"),
        "weather_main": data["weather"][0].get("main"),
        "weather_desc": data["weather"][0].get("description")
    }

    df = pd.DataFrame([cleaned])

    # Save cleaned CSV
    output_file = f"data_clean/cleaned_weather.csv"
    df.to_csv(output_file, index=False)

    print(f"[OK] Cleaned data saved -> {output_file}")

if __name__ == "__main__":
    clean_weather_data()
