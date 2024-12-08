"""
Single Inheritance
    - In single inheritance, a child class derives from one parent class.
"""
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!


"""
Multiple Inheritance -  Big difference with Java.

    - In multiple inheritance, a child class derives from more than one parent class.
"""
class LandAnimal:
    def walk(self):
        return "I can walk on land."

class WaterAnimal:
    def swim(self):
        return "I can swim in water."

class Frog(LandAnimal, WaterAnimal):
    pass

# Usage
frog = Frog()
print(frog.walk())  # Output: I can walk on land.
print(frog.swim())  # Output: I can swim in water.


"""
Method Overriding
"""
class Animal:
    def speak(self):
        return "Animal makes a sound."

class Cat(Animal):
    def speak(self):
        return "Cat says Meow!"

# Usage
cat = Cat()
print(cat.speak())  # Output: Cat says Meow!

"""
Using super()
The super() function is used to call a method from the parent class in the child class.
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Call the parent class's __init__
        self.student_id = student_id

    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} My student ID is {self.student_id}."

# Usage
student = Student("Alice", 12345)
print(student.greet())
# Output: Hello, my name is Alice. My student ID is 12345.


"""
Multi-Level Inheritance
In multi-level inheritance, a child class inherits from a parent class, and another child class inherits from that child class.
"""
class Animal:
    def eat(self):
        return "I can eat."

class Mammal(Animal):
    def walk(self):
        return "I can walk."

class Dog(Mammal):
    def bark(self):
        return "I can bark."

# Usage
dog = Dog()
print(dog.eat())   # Output: I can eat.
print(dog.walk())  # Output: I can walk.
print(dog.bark())  # Output: I can bark.


"""
Checking Inheritance with isinstance and issubclass
"""
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Mammal))  # True
print(issubclass(Dog, Animal))  # True


"""
Method Resolution Order (MRO)

In Python, the Method Resolution Order (MRO) determines the order in which classes are searched for methods and attributes. It is especially important in multiple inheritance.
	•	Use the .mro() method or help(Class) to inspect the MRO.
"""
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.show())       # Output: B
print(D.mro())        # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


