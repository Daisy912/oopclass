# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-1 20:30
class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hello")

    def display_info(self):
        print(f"Name: {self.name}")


class Customer(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age

    def greeting(self):
        print(f"Dear customers, I am {self.age} years old")


john = Customer("John Smith", 20)
john.greeting()
john.display_info()
