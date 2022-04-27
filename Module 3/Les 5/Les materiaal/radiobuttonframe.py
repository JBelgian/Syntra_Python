from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x200')

var = IntVar()
frame = LabelFrame(ws, text='Choose wisely')
frame.pack(pady=10)

Radiobutton(frame, text='Army', variable=var, value=1).grid(row=0, column=1)
Radiobutton(frame, text="Airforce", variable=var, value=2).grid(row=0, column=2)
Radiobutton(frame, text="Navy", variable=var, value=3).grid(row=1, column=1)
Radiobutton(frame, text="Seal", variable=var, value=4).grid(row=1,column=2)

ws.mainloop()
