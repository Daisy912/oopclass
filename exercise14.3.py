# student: Daisy StudentID: 202110701580008

class Pet:
    def __init__(self, type, name, number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs


f = open(r"C:\Users\admin\Desktop\my_pets.txt", "r")

my_object = []
for line in f.readlines():
    split_line = line.split(",")
    object_type = split_line[0]
    object_name = split_line[1]
    object_number = split_line[2]
    my_pets = Pet(object_type, object_name, int(object_number))
    my_object.append(my_pets)
f.close()

for object in my_object:
    print(object.type + ": " + object.name + " has " + str(object.number_of_legs) + " legs")
