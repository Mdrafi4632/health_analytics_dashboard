import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
url = "mongodb+srv://mrafi2_db_user:RafiMongo123@universitycluster.wggrv6j.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["health_data"]

print("Connected to MongoDB!")

# Function to import CSV data
def import_csv(csv_path, collection_name):
    df = pd.read_csv(csv_path)

    # Convert date columns
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Convert null to None
    df = df.where(pd.notnull(df), None)

    records = df.to_dict(orient="records")
    db[collection_name].insert_many(records)

    print(f"Inserted {len(records)} documents into '{collection_name}'")

# Fitbit Data
import_csv("data/peoples_data/daily_activity_1.csv", "daily_activity")
import_csv("data/peoples_data/daily_activity_2.csv", "daily_activity")
import_csv("data/peoples_data/sleep_day.csv", "sleep_day")

# Whoop Data
import_csv("data/rafi_data/physiologicals_rafi.csv", "physiologicals_rafi")
import_csv("data/rafi_data/sleeps_rafi.csv", "sleeps_rafi")
import_csv("data/rafi_data/workouts_rafi.csv", "workouts_rafi")