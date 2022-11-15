# student name: Daisy
# student ID: 202110701580008
def get_sum(my_list):
    if len(my_list) == 0:
        return 1
    else:
        new_list = my_list[1:len(my_list)]
        return my_list[0] * get_sum(new_list)


list1 = [1.2, 2.0, 3.5, 5.3]
sum_list = get_sum(list1)
print(sum_list)
