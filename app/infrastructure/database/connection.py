from pymongo import MongoClient
from app.core.config import MONGO_URI

from pymongo.errors import ConnectionFailure


try:
    # Initialize the client
    client = MongoClient(MONGO_URI)
    
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
    
    # Select your database and collection
    db = client["rag_app"]
    collection = db["users"]

except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")