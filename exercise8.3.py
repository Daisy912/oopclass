# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 20:52
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def message(self):
        print("Hello")

    def details(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


sam = Person("Sam", 20)
james = Person("James", 21)

sam.message()
sam.details()
james.message()
james.details()
