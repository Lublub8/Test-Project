from tkinter import *
screen=Tk()

screen.title("Division Calculator")

def divide():
    a = float(number.get())/float(number2.get())
    result.set(f'{a}')
#widget
Label(text="Division").pack()

number=Entry(screen)
number.pack()

number2=Entry(screen)
number2.pack()

Button(text="Divide",command=divide).pack()

result=IntVar()
Label(text="",textvariable=result).pack()

screen.mainloop()