# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-8 12:29
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    def __init__(self, colour):
        self.colour = colour

    def fill(self):
        print("Shape filled with {0}".format(self.colour))

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def __init__(self, colour, length, width):
        Shape.__init__(self, colour)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a rectangle")


class Circle(Shape):
    def __init__(self, colour, radius):
        Shape.__init__(self, colour)
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def draw(self):
        print("Drawing a circle")


shapes = [Circle("Blue", 10),
          Circle("White", 20),
          Rectangle("Black", 3, 5),
          Rectangle("Red", 7, 9)]

for i in shapes:
    i.fill()
    i.draw()
total_area = 0
max_area = shapes[0].get_area()

min_area = shapes[0].get_area()
for i in shapes:
    area1 = i.get_area()
    total_area = total_area + area1
    if area1 > max_area:
        max_area = area1
    if area1 < min_area:
        min_area = area1
average_area = total_area / len(shapes)

print(f"{total_area:.2f}")
print(f"{average_area:.2f}")
print(f"{max_area:.2f}")
print(f"{min_area:.2f}")
