import requests
import json
import os
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"
CITY = "London"

def fetch_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Create the folder if it doesn't exist
        os.makedirs("data_raw", exist_ok=True)

        # Create filename with timestamp
        filename = f"data_raw/weather_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

        # Save the raw JSON
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[OK] Weather data saved -> {filename}")

    else:
        print("[ERROR] Failed to fetch data:", response.text)

if __name__ == "__main__":
    fetch_weather_data()
