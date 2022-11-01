# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-18 08:13

counts = eval(input("How many sensors are currently collecting data?: "))
temperature_list = []
number = 0
for i in range(1, counts + 1):
    temperature = eval(input(f"Enter temperature {i}: "))
    temperature_list.append(temperature)
    if 10 <= temperature <= 20:
        number += 1
sums = sum(temperature_list)
average = sums / len(temperature_list)
temperature_list.sort(reverse=True)
print(f"Average temperature: {average:.2f}")
print(f"Maximum temperature: {temperature_list[0]}")
print(f"Number of temperature between 10 and 20: {number}")
