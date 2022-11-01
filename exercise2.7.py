# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-6 10:47
user_Input = input("Enter an animal:")
print(user_Input)

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number"))
Answer = num1 + num2
print(Answer)

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
Area = length * width
Perimeter = (length + width) * 2
print("Area = " + str(Area), "\nPerimeter = " + str(Perimeter))

radius = float(input("Enter the radius of the circle:"))
Area = 3.14 * radius ** 2
print("Area = " + str(Area))
