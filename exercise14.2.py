# student: Daisy StudentID: 202110701580008

f = open(r"C:\Users\admin\Desktop\my_text2.txt", "r")
my_list = []
for i in f.readlines():
    my_list.append(int(i))
f.close()

print("Sum:", str(sum(my_list)))
