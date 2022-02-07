import tkinter.messagebox
from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

def zeg_user_naam():
    tkinter.messagebox.showinfo(title="Hallo User",message=E1.get())

B1 = Button(top,text="Klik hier",command = zeg_user_naam)
B1.pack(side = RIGHT)

top.mainloop()
