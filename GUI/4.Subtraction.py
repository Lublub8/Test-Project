from tkinter import *
screen=Tk()

screen.title("Subtraction Calculator")

def subtract():
    a = float(number.get())-float(number2.get())
    result.set(f'{a}')
#widget
Label(text="Subtraction").pack()

number=Entry(screen)
number.pack()

number2=Entry(screen)
number2.pack()

Button(text="Subtract",command=subtract).pack()

result=IntVar()
Label(text="",textvariable=result).pack()

screen.mainloop()