# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 13:24

choose = "y"
Sum, count = 0, 0
while choose == "y":
    nums = int(input("Enter a number: "))
    Sum += nums
    count += 1
    choose = input("Do you want to enter another number?: ")
print(f'Sum = {Sum}')
print(f'Average = {Sum / count}')
