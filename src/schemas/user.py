"""
User Schema - This will be used to autogenerate the documentation of the API.
"""
def userEntity(userItem) -> dict:
    return {
        "id": str(userItem["_id"]), # Convert ObjectId from mongodb to string
        "name": userItem["name"],
        "email": userItem["email"],
        "password": userItem["password"],
    }

"""
Traverse the list of input users and return a list of users with the userEntity function.
"""
def usersEntity(users) -> list:
    return [userEntity(userItem) for userItem in users]