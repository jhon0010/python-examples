"""
Python Garbage Collector

The garbage collector (GC) in Python is responsible for automatic memory management. It frees up memory by collecting and disposing of objects that are no longer in use, ensuring efficient resource utilization. Python uses reference counting and a cyclic garbage collector to manage memory.
"""

"""
. Reference Counting

Python tracks how many references exist to an object. When an object’s reference count drops to zero, it is automatically destroyed.
	•	Reference Count Increases:
	•	When a new reference is created.
	•	Examples: assigning a variable, passing an object to a function.
	•	Reference Count Decreases:
	•	When a reference is deleted or goes out of scope.
"""
import sys

a = []  # Create an empty list
print(sys.getrefcount(a))  # Output: 2 (one reference by 'a', another by getrefcount)
b = a
print(sys.getrefcount(a))  # Output: 3 (new reference from 'b')
del b
print(sys.getrefcount(a))  # Output: 2 (reference 'b' removed)


"""
2. Cyclic Garbage Collection

Reference counting alone cannot handle reference cycles (e.g., two objects referencing each other). Python uses a cyclic garbage collector to identify and clean up such cycles.
"""
class Node:
    def __init__(self, name):
        self.name = name
        self.child = None

a = Node("A")
b = Node("B")
a.child = b
b.child = a  # Creates a cycle

del a
del b  # These objects will remain in memory without cyclic GC


"""
Control the GC using the gc module:
"""
import gc

gc.collect()  # Manually trigger garbage collection