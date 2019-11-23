from tkinter import *
screen=Tk()

screen.title("Calculator")

#Subtraction
def subtract():
    a = float(number1.get())-float(number2.get())
    result.set(f'{a}')
#widget
Label(text="Subtraction").grid(row=0,column=0,columnspan=2)

Label(text="1st Number").grid(row=1,column=0)
number1=Entry(screen)
number1.grid(row=1,column=1)

Label(text="2nd Number").grid(row=2,column=0)
number2=Entry(screen)
number2.grid(row=2,column=1)

Button(text="Subtract",command=subtract).grid(row=3,column=0,columnspan=2)

number = ['Number 1', 'Number 2']

r=4

for number in number:
  result = IntVar()
  Label(text="",textvariable=result).grid(row=r, column=0, sticky=NSEW,columnspan=2)
  r+=1

#Addition
def add():
    a = float(number3.get())+float(number4.get())
    result.set(f'{a}')
#widget
Label(text="Addition").grid(row=7,column=0,columnspan=2)

Label(text="1st Number").grid(row=8,column=0)
number3=Entry(screen)
number3.grid(row=8,column=1)

Label(text="2nd Number").grid(row=9,column=0)
number4=Entry(screen)
number4.grid(row=9,column=1)

Button(text="Add",command=add).grid(row=10,column=0,columnspan=2)

number = ['Number 3', 'Number 4']

r=11

for number in number:
  result = IntVar()
  Label(text="",textvariable=result).grid(row=r, column=0, sticky=NSEW,columnspan=2)
  r+=1


screen.mainloop()