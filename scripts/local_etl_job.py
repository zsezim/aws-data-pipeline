import pandas as pd
import glob

# Load data
#df = pd.read_csv("/Users/sezimzamirbekova/aws-data-pipeline/data/raw/flights-1-with-duplicates.csv")
files = glob.glob("data/raw/*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

print(df.head())
# -----------------------------
# Cleaning
# -----------------------------
df = df.dropna(subset=["DEPARTURE_TIME", "ARRIVAL_TIME", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT"])

df["DEPARTURE_TIME"] = df["DEPARTURE_TIME"].astype(int)
df["ARRIVAL_TIME"] = df["ARRIVAL_TIME"].astype(int)

df = df[(df["DEPARTURE_TIME"] > 0) & (df["DEPARTURE_TIME"] <= 2359) & (df["ARRIVAL_TIME"] > 0) & (df["ARRIVAL_TIME"] <= 2359)]

# -----------------------------
# Feature Engineering
# -----------------------------
df["route"] = df["ORIGIN_AIRPORT"] + "_" + df["DESTINATION_AIRPORT"]

def bucket_time(x):
    if 500 <= x < 1200:
        return "Morning"
    elif 1200 <= x < 1700:
        return "Afternoon"
    elif 1700 <= x <= 2359:
        return "Evening"
    elif 0 <= x < 500:
        return "Night"
    else:
        return "Unknown"

df["departure_time_bucket"] = df["DEPARTURE_TIME"].apply(bucket_time)
df["arrival_time_bucket"] = df["ARRIVAL_TIME"].apply(bucket_time)

# -----------------------------
# Deduplication
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Save output
# -----------------------------
df.to_parquet("data/processed/airlines_clean.parquet", index=False)
df.to_csv("data/processed/airlines_clean.csv", index=False)
print("ETL completed successfully")