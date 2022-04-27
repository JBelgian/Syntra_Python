from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x200')

def viewSelected():
    choice  = var.get()
    if choice == 1:
       output = "Science"

    elif choice == 2:
       output =  "Commerce"

    elif choice == 3:
       output =  "Arts"
    elif choice == 4:
        output = "IT"
    else:
        output = "Invalid selection"

    return messagebox.showinfo('PythonGuides', f'You Selected {output}.')

var = IntVar()
var2 = IntVar()
Radiobutton(ws, text="Science", variable=var, value=1, command=viewSelected).pack()
Radiobutton(ws, text="Commerce", variable=var, value=2, command=viewSelected).pack()
Radiobutton(ws, text="Arts", variable=var, value=3, command=viewSelected).pack()
Radiobutton(ws, text="IT", variable=var2, value=4, command=viewSelected).pack()

ws.mainloop()
