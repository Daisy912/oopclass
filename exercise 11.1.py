# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-1 20:32
from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, colcor):
        self.color = colcor


# Interface
class I_air_vehicle(ABC):
    @abstractmethod
    def fly(self):
        pass


# Interface
class I_land_vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Plane(Vehicle, I_air_vehicle):

    def __init__(self, colour, air_speed):
        Vehicle.__init__(self, colour)
        self.air_speed = air_speed

    def fly(self):
        return "Plane flying"


class Car(Vehicle, I_land_vehicle):
    def __init__(self, color, land_speed):
        Vehicle.__init__(self, color)
        self.land_speed = land_speed

    def drive(self):
        return "Car driving"


v1 = Plane("red", 200)
print(v1.color)
print(v1.fly())
print(v1.air_speed)

v1 = Car("green", 100)
print(v1.color)
print(v1.drive())
print(v1.land_speed)
