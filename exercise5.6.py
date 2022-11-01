# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:13
fib = []
fib.append(0)
fib.append(1)
for i in range(2, 10):
    new_num = fib[i - 1] + fib[i - 2]
    fib.append(new_num)
for i in fib:
    print(i, end=", ")