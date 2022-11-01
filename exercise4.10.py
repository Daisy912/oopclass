# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 13:03
number = int(input("Enter the number for the times table:"))
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i * j, end="\t")
    print()
