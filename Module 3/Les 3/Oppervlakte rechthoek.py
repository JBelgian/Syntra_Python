from tkinter import *
def oppervlakte():
    res=int(e1.get())*int(e2.get())
    res =str(res)+" m²"
    myText.set(res)
master = Tk()
myText=StringVar()
Label(master, text="Basis").grid(row=0, sticky=W)
Label(master, text="Hoogte").grid(row=1, sticky=W)
Label(master, text="Oppervlakte:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b = Button(master, text="Calculate", command=oppervlakte())
b.grid(row=0, column=2,columnspan=2)
mainloop()
