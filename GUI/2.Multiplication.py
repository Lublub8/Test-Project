from tkinter import *
screen=Tk()

screen.title("Multiplication Calculator")

def multiply():
    a = float(number.get())*float(number2.get())
    result.set(f'{a}')
#widget
Label(text="Multiplication").pack()

number=Entry(screen)
number.pack()

number2=Entry(screen)
number2.pack()

Button(text="Multiply",command=multiply).pack()

result=IntVar()
Label(text="",textvariable=result).pack()

screen.mainloop()