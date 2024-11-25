"""
4. Using Default and Variable Arguments

You can mix *args and **kwargs with regular arguments, but the order matters:
	1.	Regular arguments
	2.	*args
	3.	Keyword-only arguments
	4.	**kwargs
"""


"""
Using *args to Sum Numbers
"""
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(5, 10))    # Output: 15


"""
**kwargs allows you to pass a variable number of keyword arguments to a function
"""
def my_function(**kwargs):
    print(kwargs)

my_function(name="Alice", age=25, city="New York")
# {'name': 'Alice', 'age': 25, 'city': 'New York'}

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, city="New York")
"""
name: Alice
age: 25
city: New York
"""


"""
Using Default and Variable Arguments
"""
def my_function(a, b, *args, key1=None, key2=None, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"*args: {args}")
    print(f"key1: {key1}, key2: {key2}")
    print(f"**kwargs: {kwargs}")

my_function(1, 2, 3, 4, 5, key1="value1", extra="extra_value")
"""
a: 1, b: 2
*args: (3, 4, 5)
key1: value1, key2: None
**kwargs: {'extra': 'extra_value'}
"""