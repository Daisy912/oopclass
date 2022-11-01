# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-13 12:34
correctPsw = 1111  # set password
pswEntered = 0
print("Program to Check Password")

# check password
while pswEntered != correctPsw:
    pswEntered = int(input("Please enter your password:"))
print("Password accepted!")
