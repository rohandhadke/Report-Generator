from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']  # Replace 'mydatabase' with your database name
    return db
