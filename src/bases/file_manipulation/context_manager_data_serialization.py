"""
Context managers are used to manage resources, ensuring proper setup and cleanup, such as file handling, database connections, or locks.
"""



"""
Pickling and unpickling data. Pickle is a module in Python that serializes and deserializes Python objects.
"""
import pickle

# Data to be serialized
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Serialize data
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Deserialize data
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}


"""
JSON is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
Cons: Supports basic Python types only (e.g., dict, list, str, int).
"""
import json

json_string = json.dumps(data)
print(json_string)

data = json.loads(json_string)
print(data)


"""
YAML is a human-readable data serialization format that is commonly used for configuration files.
Cons: Not part of the Python standard library. You need to install the PyYAML library.
"""
import yaml

yaml_string = yaml.dump(data)
print(yaml_string)

data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(data)


"""
For more advanced use cases, you can define a context manager as a class that implements the __enter__ and __exit__ methods.
"""
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        self.connection = "DatabaseConnectionObject"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection...")
        self.connection = None

# Use the context manager
with DatabaseConnection() as conn:
    print(f"Using {conn}")