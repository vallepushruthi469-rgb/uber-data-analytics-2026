import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
file_path = os.path.join(os.path.dirname(__file__), "uber.csv")
df = pd.read_csv(file_path)

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Convert Date/Time column to datetime format
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Extract hour from Date/Time
df['Hour'] = df['Date/Time'].dt.hour

# -----------------------------
# Trips by Hour Graph
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df['Hour'], bins=24)
plt.title("Uber Trips by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Trips")
plt.show()

# Peak Hour
busiest_hour = df['Hour'].value_counts().idxmax()
print("\nPeak Hour:", busiest_hour)

# Total Trips
print("Total Trips:", len(df))

# -----------------------------
# Trips by Day Graph
# -----------------------------
df['Day'] = df['Date/Time'].dt.day

plt.figure(figsize=(8,5))
df['Day'].value_counts().sort_index().plot(kind='bar')
plt.title("Uber Trips by Day")
plt.xlabel("Day")
plt.ylabel("Number of Trips")
plt.show()

# Trips per Hour
hourly_trips = df['Hour'].value_counts().sort_index()

print("\nTrips per Hour:")
print(hourly_trips)