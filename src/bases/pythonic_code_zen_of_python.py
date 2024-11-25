"""

The Zen of Python

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


To write Pythonic code, embrace Python’s philosophy and idioms:
	•	Keep it simple and elegant.
	•	Write code that is intuitive for others to read and understand.
	•	Take advantage of Python’s built-in tools, libraries, and data structures.

Being “Pythonic” is about more than just writing working code—it’s about writing code that feels natural in Python!
"""


"""
1. Readable and Simple : Pythonic: Code should be easy to read and understand.
[expression for item in iterable if condition]
[expression-if-condition for item in iterable if condition]
"""
# Pythonic
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# Non-Pythonic
squares = []
for x in numbers:
    squares.append(x**2)

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [x for row in matrix for x in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

def double(x):
    return x * 2

doubled = [double(x) for x in numbers]
print(doubled)  # Output: [2, 4, 6, 8, 10]


"""
2. Leverages Python’s Built-in Functions : Take advantage of Python’s standard library and built-in functions for efficiency.
"""

# Pythonic
total = sum(numbers)

# Non-Pythonic
total = 0
for num in numbers:
    total += num

# Comprehension with else
modified = [x if x % 2 == 0 else -x for x in numbers]
print(modified)  # Output: [-1, 2, -3, 4, -5]


"""
3. Uses Python’s Data Structures Effectively : Utilize lists, sets, dictionaries, tuples, and other structures efficiently.
"""
# Pythonic
unique_items = set(numbers)

# Non-Pythonic
unique_items = []
for num in numbers:
    if num not in unique_items:
        unique_items.append(num)

"""
4. Follows the Zen of Python : The Zen of Python can be accessed with: import this
It includes principles like:
	•	“Beautiful is better than ugly.”
	•	“Explicit is better than implicit.”
	•	“Simple is better than complex.”
"""
import this


"""
5. Avoids Reinventing the Wheel : Use existing libraries and tools to avoid reinventing the wheel.
"""

# Pythonic
import itertools
combinations = itertools.combinations(numbers, 2)

# Non-Pythonic
combinations = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        combinations.append((numbers[i], numbers[j]))


    
"""
6. Embraces Duck Typing : Python is dynamically typed, so use duck typing to write flexible and generic code.
"""
# Pythonic
def add(a, b):
    return a + b

# Non-Pythonic
def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    return a + b


"""
7. Uses Python’s Syntax Features : Take advantage of Python’s syntax features like list comprehensions, slicing, unpacking, context managers, and generators..
"""
# Pythonic
with open('file.txt') as f:
    content = f.read()

# Non-Pythonic
f = open('file.txt')
try:
    content = f.read()
finally:
    f.close()


"""
8. Avoids Unnecessary Complexity : 	Pythonic code minimizes boilerplate and avoids overly complicated constructs.
"""
# Pythonic
if x > 0:
    print("Positive")

# Non-Pythonic
if x > 0:
    status = "Positive"
    print(status)



"""
 Pythonic Patterns for Common Tasks
"""

# Python allows unpacking of lists, tuples, and even dictionaries.
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)  # 1, 2, [3, 4, 5]

# Pythonic way to swap two variables
a, b = 1, 2
a, b = b, a

# Enumerate Instead of Range with Index
# Pythonic
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# Non-Pythonic
for i in range(len(['a', 'b', 'c'])):
    print(i, ['a', 'b', 'c'][i])


# Zip for Parallel Iteration
# Pythonic
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')


