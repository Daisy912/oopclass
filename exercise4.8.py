# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:51
userInput = input()
vowel = ["a", "e", "i", "o", "u"]
count = 0
for i in userInput:
    if i in vowel:
        print("X", end="")
        count += 1
    else:
        print(i, end="")
print()
print(f'There are {count} vowels in the word or sentence.')
