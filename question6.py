# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-18 08:23

import random

rand = random.randint(0, 20)
# print(rand)
print("Guess my secret number between 0 and 20 using 4 guesses")
user = input("separated by commas: ").split(",")
for i in user:
    if eval(i) == rand:
        print(f"You won! My secret number was: {rand}")
        break
else:
    print(f"You lost! My secret number was: {rand}")
