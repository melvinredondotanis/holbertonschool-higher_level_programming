#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Defines a base class for animals."""
    @abstractmethod
    def sound(self):
        """Abstract method that should be
        implemented in child classes."""
        pass


class Dog(Animal):
    """Defines a dog class."""
    def sound(self):
        """Defines a sound method for dogs."""
        return "Bark"


class Cat(Animal):
    """Defines a cat class."""
    def sound(self):
        """Defines a sound method for cats."""
        return "Meow"
