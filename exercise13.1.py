# student name: Daisy
# student ID: 202110701580008
def countdown(n):
    if n >= 10:
        print("Finished!")
    else:
        print(n + 1)
        return countdown(n + 1)


countdown(0)
