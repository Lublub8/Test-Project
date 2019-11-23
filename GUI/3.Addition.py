from tkinter import *
screen=Tk()

screen.title("Addition Calculator")

def add():
    a = float(number.get())+float(number2.get())
    result.set(f'{a}')
#widget
Label(text="Addition").pack()

number=Entry(screen)
number.pack()

number2=Entry(screen)
number2.pack()

Button(text="Add",command=add).pack()

result=IntVar()
Label(text="",textvariable=result).pack()

screen.mainloop()