# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:35
answer = 44
count = 5

while count > 0:
    guess = int(input("Enter a number: "))
    if guess == answer:
        print("You are correct")
        break
    count -= 1
    print("Wrong. Try again. You have " + str(count) + " more tries.")
