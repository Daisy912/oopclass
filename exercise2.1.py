# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-6 10:00
meal = 44.50
tax = 0.0675
tip = 0.15
meal = meal + meal * tax
total = meal + meal * tip
print(f'Total cost of meal: ${total:.2f}')
