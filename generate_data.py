import pandas as pd
import random
from datetime import datetime, timedelta

data = []

start_date = datetime(2024, 1, 1, 6, 0, 0)

for i in range(1000):
    dt = start_date + timedelta(minutes=random.randint(0, 10000))

    lat = round(random.uniform(40.70, 40.80), 4)
    lon = round(random.uniform(-74.05, -73.90), 4)

    data.append([
        dt.strftime("%Y-%m-%d %H:%M:%S"),
        lat,
        lon,
        "B02512"
    ])
df = pd.DataFrame(data, columns=["Date/Time", "Lat", "Lon", "Base"])

df.to_csv("uber.csv", index=False)

print("1000 records generated successfully!")