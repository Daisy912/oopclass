# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 22:26
class Person:
    number_of_people = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.number_of_people += 1
        print("Add 1 person")

    @staticmethod
    def message():
        print("Hello")

    def details(self):
        print(f"My name is {self.__name} and I am {self.__age} years old.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            print("Error - wrong name")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            print("Error - wrong age")
        else:
            self.__age = value

    @classmethod
    def count_population(cls):
        print(f"There are {Person.number_of_people} people")


Person.message()
tim = Person("Tim", 29)
tim.count_population()
alice = Person("Alice", 25)
tim.count_population()
