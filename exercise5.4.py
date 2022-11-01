# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:12
marks = {"Sam": 90.5, "Jane": 85.4, "Max": 92.3, "Alice": 64.5, "John": 69.4}
sum = 0
for i in marks:
    sum += marks[i]
print(f"Sum: {sum}")
print(f"Average: {sum / len(marks)}")