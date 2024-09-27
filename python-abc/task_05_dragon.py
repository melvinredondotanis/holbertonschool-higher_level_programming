#!/usr/bin/python3
""" Task 05: Dragon class """


class SwimMixin:
    """SwimMixin class"""
    def swim(self):
        """Swim method"""
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class"""
    def fly(self):
        """Fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""
    def roar(self):
        print("The dragon roars!")
