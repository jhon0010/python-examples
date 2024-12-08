"""
Abstract Base Classes (ABCs)

Abstract Base Classes define a blueprint for other classes. Use the abc module to create them.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# animal = Animal()  # Raises TypeError: Can't instantiate abstract class
dog = Dog()
print(dog.speak())  # Output: Woof!