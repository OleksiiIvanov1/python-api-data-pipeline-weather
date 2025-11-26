import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_weather_data():
    # Ensure output folder exists
    os.makedirs("charts", exist_ok=True)

    # Load cleaned CSV
    cleaned_file = "data_clean/cleaned_weather.csv"

    if not os.path.exists(cleaned_file):
        print("[ERROR] Cleaned data not found. Run clean_data.py first.")
        return

    df = pd.read_csv(cleaned_file)

    # Temperature chart
    plt.figure(figsize=(6,4))
    plt.bar(["Temperature", "Feels Like"], [df["temp"][0], df["feels_like"][0]])
    plt.title("Temperature Overview")
    plt.ylabel("Kelvin")
    plt.savefig("charts/temperature_chart.png")
    plt.close()
    print("[OK] Saved temperature_chart.png")

    # Humidity chart
    plt.figure(figsize=(6,4))
    plt.bar(["Humidity"], [df["humidity"][0]])
    plt.title("Humidity Level")
    plt.ylabel("%")
    plt.savefig("charts/humidity_chart.png")
    plt.close()
    print("[OK] Saved humidity_chart.png")

    # Wind Speed chart
    plt.figure(figsize=(6,4))
    plt.bar(["Wind Speed"], [df["wind_speed"][0]])
    plt.title("Wind Speed Overview")
    plt.ylabel("m/s")
    plt.savefig("charts/wind_speed_chart.png")
    plt.close()
    print("[OK] Saved wind_speed_chart.png")

if __name__ == "__main__":
    analyze_weather_data()
