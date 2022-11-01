# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 22:14
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def message(self):
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


sam = Person("Sam", 20)
james = Person("James", 21)

print(sam.name)
sam.age = 30
print(sam.age)
sam.age = 130
print(sam.age)
