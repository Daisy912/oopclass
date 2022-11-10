# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-8 12:24
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject


people = [Person("Alice", 23), Student("Carl", 19, "2017A121"), Teacher("Tom", 32, "IT")]
sum_ages = 0
largest_age, smallest_age = people[0].age, people[0].age
counts = 0
for i in people:
    sum_ages += i.age
    if i.age > largest_age:
        largest_age = i.age
    if i.age < smallest_age:
        smallest_age = i.age
    if 20 <= i.age <= 30:
        counts += 1

print(f"Sum of ages: {sum_ages}")
print(f"Largest age: {largest_age}")
print(f"Smallest age: {smallest_age}")
print(f"Number of ages between 20 and 30: {counts}")
