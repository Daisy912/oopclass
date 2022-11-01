# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-18 08:55

country_temperature = {"China": 38.5, "USA": 45.8, "Pakistan": 39.5, "Russia": 5.8}
temperature_list, count = [], 0
for i in country_temperature:
    print(f"{i}: {country_temperature[i]}")
    temperature_list.append(country_temperature[i])
    if 20 <= country_temperature[i] <= 30:
        count += 1
print()
sums = sum(temperature_list)
average = sums / len(temperature_list)
temperature_list.sort(reverse=True)
print(f"Average temperature: {average:.2f}")
print(f"Maximum temperature: {temperature_list[0]:.2f}")
print(f"Number of temperature between 20 and 30 : {count}")
