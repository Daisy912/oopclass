# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 20:56
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def message(self):
        print("Hello")

    def details(self):
        print(f"My name is {self.__name} and I am {self.__age} years old.")


sam = Person("Sam", 20)
james = Person("James", 21)

sam._Person_name = "Sam"

# print(sam.name)
print(sam._Person_name)
