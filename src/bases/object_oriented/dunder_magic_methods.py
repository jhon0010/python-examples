"""
Dunder (Double UNDERscore) Magic Methods in Python are special methods surrounded by double underscores, such as __init__, __str__, __add__, etc. These methods allow you to define custom behavior for built-in Python operations and interactions, like object creation, representation, comparison, arithmetic operations, and more.

They are also known as special methods or magic methods because they enable Python’s object-oriented and operator-overloading features.
"""
class Person:

    """
    Initialization and Representation
    """

    # Initializes an object (constructor).
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Defines the string representation (used by print()).
    def __str__(self):
        return f"{self.name}, {self.age} years old"

    #Defines the object representation (used by repr()).
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 30)
print(p)           # Output: Alice, 30 years old
print(repr(p))     # Output: Person(name=Alice, age=30)


"""
Arithmetic Operations
These methods define behavior for arithmetic and bitwise operators.
	•	__add__: For +.
	•	__sub__: For -.
	•	__mul__: For *.
	•	__truediv__: For /.
	•	__floordiv__: For //.
	•	__mod__: For %.
	•	__pow__: For **.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: Vector(4, 6)


"""
Comparison Operations
	•	__eq__: For ==.
	•	__ne__: For !=.
	•	__lt__: For <.
	•	__le__: For <=.
	•	__gt__: For >.
	•	__ge__: For >=.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1 == p2)  # Output: False
print(p1 < p2)   # Output: False


"""
Container-Like Behavior

These methods make custom objects behave like Python containers (lists, dictionaries, etc.).
	•	__len__: Defines the behavior of len().
	•	__getitem__: For indexing (obj[key]).
	•	__setitem__: For assigning to an index (obj[key] = value).
	•	__delitem__: For deleting an item (del obj[key]).
	•	__contains__: For in.
"""
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items

cl = CustomList([1, 2, 3])
print(len(cl))       # Output: 3
print(cl[1])         # Output: 2
cl[1] = 42
print(cl[1])         # Output: 42
del cl[1]
print(cl.items)      # Output: [1, 3]
print(3 in cl)       # Output: True




"""
Context Managers

These methods define behavior when using the with statement.
	•	__enter__: Defines the setup code.
	•	__exit__: Defines the teardown code.

When to Use Context Managers?    
    • Context managers in Python (with statement) handle setup and teardown actions. Rewriting their behavior is useful when you need to manage resources like files, database connections, or locks in a custom way. 
"""
class ManagedResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

with ManagedResource() as resource:
    print("Using resource")


"""
Advanced Use Case: Database Connection

Heres an example of rewriting context manager behavior for database connections:
"""
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def __enter__(self):
        print(f"Connecting to database at {self.connection_string}")
        self.connection = f"Connection({self.connection_string})"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")
        if exc_type:
            print(f"Error occurred: {exc_value}")
        self.connection = None

# Usage
with DatabaseConnection("localhost:5432") as conn:
    print(f"Using {conn}")
    # Raise an error to see exception handling:
    # raise RuntimeError("Query failed")



"""
Overriding Collections (list, tuple, etc.)

You can create a subclass of list, tuple, or any other collection type and override its methods to customize its behavior.

When to Override Collections?
	1.	Validation or Restrictions: Enforce rules about what can be added to the collection (e.g., restricting data types).
	2.	Additional Features: Add extra functionality like logging, transformation, or caching.
	3.	Domain-Specific Behavior: Create specialized collection types for specific use cases, such as a matrix, graph, or priority queue.
"""
class CustomList(list):
    def append(self, item):
        if isinstance(item, str):  # Restrict to only strings
            super().append(item)
        else:
            raise ValueError("Only strings are allowed!")

    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return super().__getitem__(index)

# Usage
my_list = CustomList(["hello", "world"])
my_list.append("Python")
print(my_list[1])  # Output: Accessing index 1
# my_list.append(42)  # Raises ValueError: Only strings are allowed!



"""
**********************************************
Advanced Magic Methods
**********************************************
"""

"""
Customizing Object Behavior
	•	__del__: Called when an object is garbage collected.
"""
class Person:
    def __del__(self):
        print("Person object deleted")


"""
•	__copy__ and __deepcopy__: Customize copying behavior with the copy module.
2.	Operator Overloading
You can define behavior for more operators:
	•	__iadd__: For in-place addition (+=).
	•	__imul__: For in-place multiplication (*=).

.	Descriptor Protocol
	•	__get__, __set__, and __delete__: Used to create custom behavior for attribute access in classes.
"""

class Descriptor:
    def __get__(self, instance, owner):
        return "Getting the attribute"
class MyClass:
    attr = Descriptor()
obj = MyClass()
print(obj.attr)  # Output: Getting the attribute


"""
	Metaprogramming with __new__
	•	__new__ controls object creation before initialization (__init__).
"""
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Output: True


"""
Customizing Copying Behavior with __copy__ and __deepcopy__

When you use the copy module, Python provides two types of copies:
	1.	Shallow Copy (copy.copy):
	•	Creates a new object but does not copy nested objects.
	•	References to nested objects are shared.
	2.	Deep Copy (copy.deepcopy):
	•	Creates a new object and recursively copies all nested objects.
"""
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Shallow copy invoked")
        new_obj = type(self)(self.value)  # Create a new instance
        return new_obj

obj = MyClass(10)
shallow_copy = copy.copy(obj)  # Output: Shallow copy invoked

import copy

class MyClass:
    def __init__(self, value, nested):
        self.value = value
        self.nested = nested

    def __deepcopy__(self, memo):
        print("Deep copy invoked")
        new_obj = type(self)(
            self.value,
            copy.deepcopy(self.nested, memo)  # Deep copy nested objects
        )
        return new_obj

nested = [1, 2, 3]
obj = MyClass(10, nested)
deep_copy = copy.deepcopy(obj)  # Output: Deep copy invoked
