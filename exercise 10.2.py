# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-1 20:31
class Animal:
    def __init__(self, type):
        self.type = type

    def sound(self):
        print("No,sound")

    def display_info(self):
        print(f"Type: {self.type}")


class Dog(Animal):
    def __init__(self, type, weight):
        Animal.__init__(self, type)
        self.weight = weight

    def sound(self):
        print("Woof")


class Cat(Animal):
    def __init__(self, type, color):
        Animal.__init__(self, type)
        self.color = color

    def sound(self):
        print("Meow")


my_dog = Dog("Labrador", 22)
my_dog.sound()
my_dog.display_info()

my_cat = Cat("Siamese", "white")
my_cat.sound()
my_cat.display_info()
