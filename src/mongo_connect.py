from turtle import update
from pymongo import MongoClient
from bson.son import SON

def main():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.test_database
    print("Connected to MongoDB!")

    people_collection = db.people


    john_inserted_id = people_collection.insert_one({"name": "John", "age": 30}).inserted_id
    print("Jhon inserted id = ", john_inserted_id)
    people_collection.insert_one({"name": "Peter", "age": 30})

    # find all people and print them
    print("Find all people and print them")
    for person in people_collection.find():
        print(person)

    # find one person by id
    print("Find one person by id")
    print(people_collection.find_one({"_id": john_inserted_id}))    

    # find one person by age less than 30, lt = less than
    print("Find one person by age less than 30")
    print(people_collection.find_one({"age": {"$lt": 30}}))

    # find one person by name
    print("Find one person by name")
    print(people_collection.find_one({"name": "Peter"}))

    # Count people by name John
    print("Count people by name John")
    print(people_collection.count_documents({"name": "John"}))


    # Update one person by name, set = update
    print("Update one person by name")
    update_result = people_collection.update_one({"name": "John"}, {"$set": {"name": "John Smith"}})
    print("Update result = ", update_result)

    # Group and sort people by average age and id
    print("Group and sort people by average age and id")
    pipeline = [
        {
            "$group": {
                "_id": "$name",
                "average_age": {"$avg": "$age"}
            }
        },
        {
            "$sort": SON([("average_age", -1), ("_id", -1)])
        }
    ]
    # aggregate = group and sort in mongodb, receive a list of pipeline
    print(list(people_collection.aggregate(pipeline)))


if __name__ == "__main__":
    main()


