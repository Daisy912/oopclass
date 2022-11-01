# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 20:44
class Person:
    name = ""
    age = 0

    def message(self):
        print("Hello")

    def details(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


sam = Person()
sam.name = "Sam"
sam.age = 20
james = Person()
james.name = "James"
james.age = 21
sam.message()
sam.details()
james.message()
james.details()
