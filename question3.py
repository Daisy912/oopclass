# @name: Daisy StudentId: 202110701580008
# @Date: 2022-10-18 08:03

score = eval(input("Enter the score: "))
if 0 <= score < 50:
    print("Grade is Fail")
elif score < 60:
    print("Grade is D")
elif score < 70:
    print("Grade is C")
elif score < 80:
    print("Grade is B")
elif score < 90:
    print("Grade is A")
elif score <= 100:
    print("Grade is A+")
else:
    print("Please enter a score between 0 and 100")
