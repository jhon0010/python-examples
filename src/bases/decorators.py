"""
Decorators are a powerful tool in Python to modify or extend the behavior of functions or methods.
Decorators allow you to wrap another function to extend its behavior without modifying it.
"""

# Decorator to log function calls
def log_decorator(func):
    """
    Decorator to log function calls
        Args:
            func: The function to be decorated
        Returns:
            The wrapper function
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

# Apply the decorator
@log_decorator
def add(a, b):
    return a + b

# Call the decorated function
add(2, 3)


import time

def timing_decorator(func):
    """
    Decorator to measure the time a function takes to execute
        Args:
            func: The function to be measured
        Returns:
            The wrapper function
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done!"

slow_function()


"""
Decorator with Arguments
You can create decorators that take arguments themselves:
"""
def repeat(n):
    """
    Decorator to repeat a function call n times
        Args:
            n: The number of times to repeat the function call
        Returns:
            The decorator function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello, World!")

greet()