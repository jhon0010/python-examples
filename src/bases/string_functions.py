"""
The following class contains functions that are used to manipulate strings.
"""

# String Formatting
print("hello".center(10, '-'))  # Output: --hello---
print("hello".ljust(10, '-'))  # Output: hello-----
print("hello".rjust(10, '-'))  # Output: -----hello
print("hello".zfill(10))  # Output: 00000hello


# String Searching
print("hello".startswith("he"))  # Output: True
print("hello".endswith("lo"))  # Output: True
print("hello".find("l"))  # Output: 2
print("hello".rfind("l"))  # Output: 3
print("hello".index("l"))  # Output: 2
print("hello".rindex("l"))  # Output: 3
print("hello".count("l"))  # Output: 2


# String Modification
print("hello".capitalize())  # Output: Hello
print("hello".upper())  # Output: HELLO
print("hello".lower())  # Output: hello
print("hello".swapcase())  # Output: HELLO
print("hello".title())  # Output: Hello
print("hello".replace("l", "r"))  # Output: herro
print("hello".strip("o"))  # Output: hell
print("hello".lstrip("h"))  # Output: ello
print("hello".rstrip("o"))  # Output: hell
print("hello".partition("l"))  # Output: ('he', 'l', 'lo')
print("hello".rpartition("l"))  # Output: ('hel', 'l', 'o')
print("hello".split("l"))  # Output: ['he', '', 'o']
print("hello".rsplit("l"))  # Output: ['he', '', 'o']
print("hello".splitlines())  # Output: ['hello']
print("hello".join(["a", "b", "c"]))  # Output: ahellobhelloc

print("banana".count("a"))  # Output: 3
