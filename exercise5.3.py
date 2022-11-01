# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:12
student = dict()
student["Name"] = "James"
student["Age"] = 21
student["Course"] = "IT"
student["ID"] = "2016A001"
print(student)
print(student["Name"] + ":" + student["ID"])
del student["Course"]
for i in student:
    print(student[i])