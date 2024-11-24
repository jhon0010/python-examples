
from collections import namedtuple

"""
	•	A tuple is an ordered collection of elements, similar to a list.
	•	Immutable: Once created, its elements cannot be changed, added, or removed.
			- You cannot directly modify a tuple, but if it contains mutable objects (like a list), the contents of those objects can be changed.
	•	Defined using parentheses () or the tuple() constructor.
	•	Tuples can store heterogeneous data (elements of different types).
	•	Defined using parentheses () or the tuple() constructor.

	Comparation : Tuples are compared lexicographically, meaning the comparison is done element by element from left to right.

	Because tuples are immutable, they are hashable if all their elements are hashable. This makes them usable as:
"""

# Creation tuples
t = 1, 2, 3  # Equivalent to (1, 2, 3)
empty = ()
single = (1,)  # Note the comma
not_a_tuple = (5)  # This is an integer
t = (10, 20, 30)

# accessing tuples
print(t[0])  # Output: 10
t = (10, 20, 30, 40, 50)
print(t[1:4])  # Output: (20, 30, 40)
print(t[-1])  # Output: 50 (last element)

# concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)

# repetition
t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

# membership testing
t = (1, 2, 3)
print(2 in t)  # Output: True

t = (1, 2, 2, 3)
print(t.count(2))  # Output: 2

t = (1, 2, 3)
print(t.index(3))  # Output: 2

# Tuple Packing and Unpacking
t = (1, 2, 3)
a, b, c = t  # Unpacking
print(a, b, c)  # Output: 1 2 3

"""
 Use Cases of Tuples

	•	Immutable Data: Protect data from accidental modification.
	•	Dictionary Keys: Since tuples are hashable, they can serve as dictionary keys.
"""
locations = {(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}



# Nested Tuples 
nested = (1, (2, 3), (4, (5, 6)))
print(nested[1][1])  # Output: 3
print(nested[3][1][0])  # Output: 5


# Tuple as a Return Value

def min_max(nums):
	return min(nums), max(nums)

result = min_max([83, 33, 84, 32, 85, 31, 86])
print(result)  # Output: (31, 86)


# Comparison of Tuples 
# Tuples are compared lexicographically, meaning the comparison is done element by element from left to right.
t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(t1 < t2)  # Output: True (because 3 < 4)
print(t1 == t2)  # Output: False



# Set elements

unique_points = {(1, 2), (3, 4), (1, 2)}  # Automatically removes duplicates
print(unique_points)  # Output: {(1, 2), (3, 4)}


# Sorting a List of Tuples

students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]
students_sorted = sorted(students, key=lambda x: x[1])  # Sort by age
students_sorted_by_name = sorted(students, key=lambda x: x[0])  # Sort by name
print(students_sorted)  # Output: [('Bob', 22), ('Charlie', 23), ('Alice', 25)]
print(students_sorted_by_name)  # Output: [('Alice', 25), ('Bob', 22), ('Charlie', 23)]

# Tuple of Tuples

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix[1][2])  # Output: 6 (2nd row, 3rd column)


"""
For readability and improved code semantics, namedtuple from the collections module is a powerful extension of tuples.
"""
# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create instances
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20


# Representing Fixed Collections
RGB = (255, 0, 0)  # Red color in RGB
BLACK = (0, 0, 0)  # Black color in RGB


# Tuple Unpacking
x, y = (10, 20)
print(x, y)  # Output: 10 20

# Modifying Tuples: Not Possible
# You cannot directly modify a tuple, but if it contains mutable objects (like a list), the contents of those objects can be changed.
t = (1, [2, 3])
t[1].append(4)
print(t)  # Output: (1, [2, 3, 4])