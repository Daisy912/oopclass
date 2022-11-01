# @name: Daisy StudentId: 202110701580008
# @Date: 2022-9-27 14:20
from tkinter import *
root =Tk()

def calcC():
    user_text=float(myEntry.get())
    new_temp=user_text*1.8+32
    return myLable.config(text=str(new_temp))

def calcF():
    user_text=float(myEntry.get())
    new_temp=(user_text-32)/1.8
    return myLable.config(text=str(new_temp))

myEntry=Entry()
myLable=Label(text="")
buttom1=Button(text="Celsius",fg="red",command=calcC)
buttom2=Button(text="Fahrenheit",fg="green",command=calcF)


myEntry.pack()
myLable.pack()
buttom1.pack(side=LEFT)
buttom2.pack(side=LEFT)

root.mainloop()