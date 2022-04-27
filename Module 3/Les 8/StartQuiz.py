import Quiz
from tkinter import *

# Creeert GUI Window
gui_start = Tk()

# zet de groote van GUI Window
gui_start.geometry("800x450")


def open_admin():
    gui_admin = Tk()
    gui_admin.geometry("800x450")


def open_quiz():
    Quiz.startquiz()


adm_btn = Button(gui_start, text="Admin", command=open_admin, width=10, bg="blue", fg="white",
                 font=("ariel", 16, "bold"))
adm_btn.place(x=100, y=300)

quiz_btn = Button(gui_start, text="Quiz", command=open_quiz, width=10, bg="blue", fg="white",
                  font=("ariel", 16, "bold"))
quiz_btn.place(x=400, y=300)

gui_start.mainloop()
