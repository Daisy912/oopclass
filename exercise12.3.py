# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-8 12:29
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


workers = [Worker("Tim", 65000), Worker("Jane", 52000), Worker("Sam", 48000)]
sum_salary = 0
largest_salary, smallest_salary = workers[0].salary, workers[0].salary
counts = 0
for i in workers:
    sum_salary += i.salary
    if i.salary <= smallest_salary:
        smallest_salary = i.salary
    if i.salary >= largest_salary:
        largest_salary = i.salary
    if 50000 <= i.salary <= 70000:
        counts += 1

print(f"Sum of the salaries: {sum_salary}")
print(f"Largest salary: {largest_salary}")
print(f"Smallest salary: {smallest_salary}")
print(f"Number of salaries between 50000 and 70000: {counts}")
