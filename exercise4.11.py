# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 13:11
week = ["M", "T", "W", "T", "F", "S", "Su"]
for i in week:
    print(i, end="\t")
print()
for i in range(1, 32):
    print(i, end="\t")
    if i % 7 == 0:
        print()
