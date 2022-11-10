# @name: Daisy StudentId: 202110701580008
# @Date: 2022-11-8 12:23
student_marks = []
student_marks.extend((75, 87, 74, 63, 87, 71))
student_marks[2] = 55
counts = 0
for i in student_marks:
    print(i)
    if 70 <= i <= 80:
        counts += 1
sum_marks = sum(student_marks)
average = sum_marks / len(student_marks)

print(f"Sum: {sum_marks}")
print(f"Average: {average}")

student_marks.sort(reverse=True)

print(f"Largest mark: {student_marks[0]}")
print(f"Smallest mark: {student_marks[len(student_marks) - 1]}")
print(f"There are {counts} marks between 70 and 80")
