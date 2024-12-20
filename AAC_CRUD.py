from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCRUD:
    def __init__(self, username, password, host, port, database, collection):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection

        # Connect to the MongoDB server
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
        self.db = self.client[database]
        self.collection = self.db[collection]

    
    #Create method -- creates documents in database
    def create(self, data):
        try: 
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False

    #Read method -- reads documents from database
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print (f"Error querying documents: {e}")
            return []
          
    #Update method - finds documents in database and makes changes
    def update(self, query, data):
        try:
            result = self.collection.update_many(query, {'$set': data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating document: {e}")
            return 0
    
    #Delete method - finds documents in database and removes
    def delete(self, query):
        try: 
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0
