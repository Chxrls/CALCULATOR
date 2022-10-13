from os import execv
from tkinter import *
import math as m
from webbrowser import get

def button_detect(number):
    global text_variable

    text_variable = text_variable + str(number)
    text_display.set(text_variable)
#    error.config(text="INPUT DETECTED")

def equals():
    global text_variable

    try:
        answer = str(eval(text_variable))
        text_display.set(answer)
        text_variable = answer

    except SyntaxError:
        text_display.set("")
        text_variable = ""
        error.config(text="SYNTAX ERROR")

    except ZeroDivisionError:
        text_display.set("get some help")
        text_variable = ""
        error.config(text="UNDEFINED")

    except TypeError:
        text_display.set("")
        text_variable = ""
        error.config(text="USE CORRECT OPERATORS")

def square():
    global text_variable

    try:
       sqrtnum = text_variable
       sqrtresult = m.sqrt(sqrtnum)
       text_display.set(sqrtresult)
       error.config(text="SQUARE ROOT")

    except:
        text_display.set("")
        text_variable = ""
        error.config(text="SYNTAX ERROR")

def clear():
    global text_variable
    text_display.set("")
    text_variable = ""
    error.config(text="")

calculator = Tk()
calculator.title("Calculator | Charls")
calculator.geometry("420x300")
calculator.resizable(0,0)
icon = PhotoImage(file='calculator.png')
calculator.iconphoto(True,icon)

text_variable = ""

text_display = StringVar()

label = Label(calculator,textvariable=text_display,bg="#c1cbdb",font=("Arial",25,"bold"),bd=10,relief=SUNKEN, width=33)
label.pack()
frame = Frame(calculator)
frame.pack()

#digits
num1 = Button(frame,text=1,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(1))
num1.grid(row=1,column=1)

num2 = Button(frame,text=2,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(2))
num2.grid(row=1,column=2)

num3 = Button(frame,text=3,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(3))
num3.grid(row=1,column=3)

num4 = Button(frame,text=4,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(4))
num4.grid(row=2,column=1)

num5 = Button(frame,text=5,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(5))
num5.grid(row=2,column=2)

num6 = Button(frame,text=6,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(6))
num6.grid(row=2,column=3)

num7 = Button(frame,text=7,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(7))
num7.grid(row=3,column=1)

num8 = Button(frame,text=8,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(8))
num8.grid(row=3,column=2)

num9 = Button(frame,text=9,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(9))
num9.grid(row=3,column=2)

num0 = Button(frame,text=0,font=("Arial",10),width=6,height=3,bd=3,bg="#91a6c7",command=lambda: button_detect(0))
num0.grid(row=3,column=3)

dot = Button(frame,text="•",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("."))
dot.grid(row=3,column=5)

#operators
add = Button(frame,text="+",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("+"))
add.grid(row=1,column=4)

subtract = Button(frame,text="—",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("-"))
subtract.grid(row=1,column=5)

multiply = Button(frame,text="x",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("*"))
multiply.grid(row=2,column=4)

divide = Button(frame,text="/",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("/"))
divide.grid(row=2,column=5)

exponent = Button(frame,text="^",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("**"))
exponent.grid(row=1,column=6)

squarer = Button(frame,text="√",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=square)
squarer.grid(row=2,column=6)

result = Button(frame,text="=",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=equals)
result.grid(row=3,column=4)

openp = Button(frame,text="(",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect("("))
openp.grid(row=1,column=7)

closep = Button(frame,text=")",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=lambda: button_detect(")"))
closep.grid(row=2,column=7)

#delete
delete = Button(frame,text="clear",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=clear)
delete.grid(row=3,column=6)

#backspc = Button(frame,text="<-",font=("Arial",10),width=6,height=3,bd=3,bg="#5ca3bd",command=backspace)
#backspc.grid(row=3,column=7)

#error display
error = Label(font=("Arial",10),width=30,height=3)
error.pack()

calculator.mainloop()
