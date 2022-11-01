# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:40
studentNum = int(input("Enter the number of student grades:"))

# loop for the number of students
for i in range(0, studentNum):
    grade = int(input(f'Enter grade {i+1}:'))
    if grade >= 50:
        print("Student has passed")
    else:
        print("Student has failed")
