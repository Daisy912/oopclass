# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-1 20:32
from abc import ABC, abstractmethod


class Electronic(ABC):
    def __init__(self, company):
        self.company = company

    @abstractmethod
    def turn_on(self):
        pass


class Smartphone(Electronic):
    def __init__(self, company, GB):
        Electronic.__init__(self, company)
        self.GB = GB

    def turn_on(self):
        print("Hold button on side")


class TV(Electronic):
    def __init__(self, company, size):
        Electronic.__init__(self, company)
        self.size = size

    def turn_on(self):
        print("Push button on remote")


e1 = Smartphone("Meizu", 64)
e2 = TV("Samsung", 50)
e1.turn_on()
e2.turn_on()
