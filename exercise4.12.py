# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 13:18
for i in range(8):  # do this 8 times
    # print spaces first
    for j in range(0, 7 - i):  # go from 0 to 7-i
        print(" ", end="")  # print space on same line

    # print stars
    for k in range(0, (2 * i + 1)):  # go from 0 to (2*i + 1)
        print("*", end="")  # print star on same line
    print()  # print a new line

# now print the bottom half of the diamond
for i in range(6, -1, -1):
    for j in range(0, 7 - i):
        print(" ", end="")

        # print stars
    for k in range(0, (2 * i + 1)):
        print("*", end="")
    print()
