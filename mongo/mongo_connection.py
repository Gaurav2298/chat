from pymongo import MongoClient

# Replace the connection string with your MongoDB connection string
uri = "mongodb://localhost:27017/chat"

# Create a MongoClient
client = MongoClient(uri)

try:
    # Connect to the MongoDB server
    db = client.get_database()
    print("Connected to MongoDB")

    # Access your database or perform other operations here

finally:
    # Close the connection when you're done
    client.close()
    print("Connection to MongoDB closed")
