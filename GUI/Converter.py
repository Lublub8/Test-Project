from tkinter import *
screen=Tk()

screen.title("Measurement Convertor Software")

def convert():
    cm = float(inches.get())*2.54
    result.set(f'{cm} cm')
#widget
Label(text="Inches to Centimetre Convertor").pack()

inches=Entry(screen)
inches.pack()

Button(text="Convert",command=convert).pack()

result=IntVar()
Label(text="",textvariable=result).pack()

screen.mainloop()