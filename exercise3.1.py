# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:31
print("Program to show high and low numbers")

# Get input and calculate number
num1 = int(input("Enter a number"))
if num1 > 50:
    print(str(num1) + " is a high number")
if num1 < 50:
    print(str(num1) + " is a low number")
if num1 == 50:
    print(f"{num1} is in the middle")
