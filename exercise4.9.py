# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:59
userInput = input("Please enter a word or sentence:")
for i in userInput:
    if i == "x":
        print("This has the letter ‘x’ in it")
        break
else:
    print("This does not have the letter ‘x’ in it")
