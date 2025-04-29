# app/config.py
import os
from pymongo import MongoClient

# Fetch MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database()  # Use your database name
