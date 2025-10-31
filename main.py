import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":

    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    print(f"Площадь прямоугольника: {rectangle.area()}")  # 15
    print(f"Площадь круга: {circle.area():.2f}")  # 50.27
