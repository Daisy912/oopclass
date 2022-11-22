# student: Daisy StudentID: 202110701580008

try:
    x = int(input("Please enter a number: "))

except ValueError as my_err:
    print("That was not valid number.  Try again...")
    exit(0)  # stop program

try:
    f = open("my_numbers.txt", "r")

except IOError as my_err:
    print("Cannot find file")                     
    exit(0)  # stop program

file = open("my_numbers.txt", "r")
line_list = file.read().split()
y = int(line_list[1])

try:
    z = x / y
except ZeroDivisionError as my_err:
    print("You cannot divide by zero")
    exit(0)  # stop program
