# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:14
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

myLable = Label(topFrame, text="Do not click the OK button!",fg="red")
myButtom1 = Button(bottomFrame, text="OK", fg="green")
myButtom2 = Button(bottomFrame, text="Cancel", fg="blue")

myLable.pack()
myButtom1.pack(side=LEFT)
myButtom2.pack(side=LEFT)

root.mainloop()
