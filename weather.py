import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------- LOAD DATA --------
df = pd.read_csv("weather_data.csv", parse_dates=["date"])

# -------- BASIC ANALYSIS --------
print("Summary Statistics:\n", df.describe())

# Calculate rolling averages (smoothing)
df["temp_avg"] = df["temperature"].rolling(window=3).mean()
df["humidity_avg"] = df["humidity"].rolling(window=3).mean()

# -------- VISUALIZATION --------
plt.figure(figsize=(14, 8))

# Temperature trend
plt.subplot(3, 1, 1)
plt.plot(df["date"], df["temperature"], label="Daily Temp", color="tab:red", marker="o")
plt.plot(df["date"], df["temp_avg"], label="3-Day Avg", color="tab:orange", linestyle="--")
plt.ylabel("Temperature (°C)")
plt.title("Weather Analysis")
plt.legend()
plt.grid(True)

# Humidity trend
plt.subplot(3, 1, 2)
plt.plot(df["date"], df["humidity"], label="Daily Humidity", color="tab:blue", marker="x")
plt.plot(df["date"], df["humidity_avg"], label="3-Day Avg", color="tab:cyan", linestyle="--")
plt.ylabel("Humidity (%)")
plt.legend()
plt.grid(True)

# Wind speed distribution (histogram)
plt.subplot(3, 1, 3)
plt.hist(df["wind_speed"], bins=np.arange(0, max(df["wind_speed"])+2, 2), 
         color="tab:purple", alpha=0.7, edgecolor="white")
plt.xlabel("Wind Speed (km/h)")
plt.ylabel("Frequency")
plt.title("Wind Speed Distribution")

plt.tight_layout()
plt.show()
