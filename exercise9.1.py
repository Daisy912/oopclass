# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-30 22:56
class Person:

    def __init__(self, name):
        self.name = name

    # <Make a method say_name>
    #     <It will print "Hi, my name is ...">
    def say_name(self):
        print(f"Hi, my name is {self.name}")


class Student(Person):

    def __init__(self, name, id):
        Person.__init__(self, name)
        self.id = id


# <Make a class called Worker that inherits the Person class>
class Worker(Person):
    # <Make the __init__ method with a new parameter called salary>
    #    <Call the __init__ method of the Person class>
    #    <Make the object variable for salary>

    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary


student1 = Student("James", "2016A1234")
print(student1.name)
print(student1.id)
# <Call the say_name() method on the student1 object>


student1.say_name()

# <Make a worker object called worker1 with the name "Max" and a salary of 30000>
# <Print out the name of the worker>
# <Print out the salary of the worker>
# <Call the say_name() method on the worker1 object>

worker1 = Worker("Max", 30000)
print(worker1.name)
print(worker1.salary)
worker1.say_name()
