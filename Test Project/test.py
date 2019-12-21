
from tkinter import *
from tkinter.ttk import *
root=Tk()

s=Style()
s.theme_use('clam')

s.configure('.', font=('verdana', 14),background='lightblue')
s.configure('TEntry',foreground='darkblue')
s.configure('TLabel',foreground='black',background='lightblue')
s.configure('TFrame',foreground='white',background='lightblue')
s.configure('TProgressbar',background='green')
s.map('TButton',background=[('pressed','lightblue'),('active','white')],foreground=[('pressed','red'),('active','blue')])
######################################################

root.configure(background='lightblue')
root.geometry("510x600")
root.title("File Explorer App")
root.resizable(False,False)

def formdata():
    print(f'Combo Box:      {cmbvar.get()}')

Label(root,text="File Explorer App",background='lightgreen').pack()

#Document
Tab1=Notebook(root,width=500)
Tab1.pack()

NewFrame = Frame(Tab1)
Tab1.add(NewFrame,text="Document")

#Pictures
Tab2=Notebook(root,width=500)
Tab2.pack()

NewFrame2 = Frame(Tab2)
Tab2.add(NewFrame2,text="Pictures")

#Music
Tab3=Notebook(root,width=500)
Tab3.pack()

NewFrame3 = Frame(Tab3)
Tab3.add(NewFrame3,text="Music")

#Video
Tab4=Notebook(root,width=500)
Tab4.pack()

NewFrame4 = Frame(Tab4)
Tab4.add(NewFrame4,text="Video")


file_ex = 'File Extensions'

Label1 = Label(NewFrame, text=file_ex, style='TLabel')
Label1.grid(row=0, column=0, sticky=NSEW)

Opt_doc = ['.DOCX','.TXT','.PDF','.ODT','.RTF','.HTML','.PPTX']
Opt_pic = ['.JPG','.PNG','.GIF','.TIFF','.PSD','.EPS','.AI','.INDD','.RAW']
Opt_mus = ['.WAV','.MP3','.WMA','.AAC','.FLAC','.MID','.MIDI']
Opt_vid = ['.MPEG','.MP4','.3GP','.OGG','.WMV','.WEBM','.HDV']

#Document
cmbvar1=StringVar(NewFrame)
cmbvar1.set(Opt_doc[0])
Combo1=Combobox(NewFrame,height=10,width=25,values=Opt_doc,textvariable=cmbvar1) #Height refers to number of values it will list without scroll
Combo1.grid(row=6,column=1,columnspan=2,sticky=NSEW)

#Pictures
cmbvar2=StringVar(NewFrame2)
cmbvar2.set(Opt_pic[0])
Combo2=Combobox(NewFrame2,height=10,width=25,values=Opt_pic,textvariable=cmbvar2) #Height refers to number of values it will list without scroll
Combo2.grid(row=6,column=1,columnspan=2,sticky=NSEW)

#Music
cmbvar3=StringVar(NewFrame3)
cmbvar3.set(Opt_mus[0])
Combo3=Combobox(NewFrame3,height=10,width=25,values=Opt_mus,textvariable=cmbvar3) #Height refers to number of values it will list without scroll
Combo3.grid(row=6,column=1,columnspan=2,sticky=NSEW)

#Video
cmbvar4=StringVar(NewFrame4)
cmbvar4.set(Opt_vid[0])
Combo4=Combobox(NewFrame4,height=10,width=25,values=Opt_vid,textvariable=cmbvar4) #Height refers to number of values it will list without scroll
Combo4.grid(row=6,column=1,columnspan=2,sticky=NSEW)
