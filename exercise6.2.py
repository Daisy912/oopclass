# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:14
from tkinter import *
import tkinter.messagebox


def showName():
    user_text = Entry.get(myEntry)
    return tkinter.messagebox.showinfo("My name", user_text)


def changeName():
    myEntry.delete(0,END)
    myEntry.insert(0,"Sam")

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
myLable = Label(topFrame, text="Enter your name:")
myEntry = Entry(topFrame)
myList = Listbox(topFrame)
myList.insert(0, "Male")
myList.insert(1, "Fmale")

myButtom1 = Button(bottomFrame, text="Show name", fg="red", command=showName)
myButtom2 = Button(bottomFrame, text="Change name", fg="green", command=changeName)

myButtom1.pack(side=LEFT)
myButtom2.pack(side=LEFT)

myLable.pack()
myEntry.pack()
myList.pack()
root.mainloop()
