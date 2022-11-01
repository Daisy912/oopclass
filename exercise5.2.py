# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:11
n = int(input("Enter the number of values to insert: "))
myList = []
for i in range(0, n):
    get_num = int(input("Enter a number to insert: "))
    myList.append(get_num)
sum = sum(myList)
average = sum / len(myList)
print(f'Sum is: {sum}')
print(f'Average is: {average}')
