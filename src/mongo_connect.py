from pymongo import MongoClient

def main():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.test_database
    print("Connected to MongoDB!")

if __name__ == "__main__":
    main()


