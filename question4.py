# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-18 08:09

letter_message = {"k": "King", "q": "Queen", "j": "Jack", "a": "Ace"}
while True:
    user = input("Enter a card letter: ").lower()
    if user in letter_message:
        print(letter_message[user])
        break
    else:
        print("Try again.")
