# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:36
i = 3  # counter for number of logins
done = False
print("Program to Change Password")
print("Your password has expired and you have " + str(i) + " chances left to change your password")

# While password is not entered correctly AND more than 0 chances
while not done and i > 0:
    newPsw = input("Please enter your new password: ")

    pswEntered = input("Please enter password again to confirm:")
    # change password correct
    if pswEntered == newPsw:
        done = True
    else:
        print("Error in entering password, please try again")
        i -= 1
        print(f"you have i chances left")

if i <= 0:
    print("Password not changed")  # password accepted
else:
    print("Password accepted!")
