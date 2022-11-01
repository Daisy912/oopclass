# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-18 08:31

print("Enter the first line of numbers separated by commas:")
list1 = input().split(",")
print("Enter the second line of numbers separated by commas:")
list2 = input().split(",")
counts = 0
for i in list1:
    for j in list2:
        if i == j:
            counts += 1
print(f"There are {counts} numbers that are in both lists")
