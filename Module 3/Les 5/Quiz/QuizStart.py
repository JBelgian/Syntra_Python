from tkinter import *


guiStart = Tk()
guiStart.title("Admin or Quizzer")


def openAdmin():
    adm = Toplevel()
    adm.title("Admin window")
    btn_close = Button(adm, text="Close window", command=adm.destroy)
    btn_close.place(x=0, y=0)


def openQuiz():


btn_adm = Button(guiStart, text="Admin", command=openAdmin)
btn_adm.place(x=0, y=0)

btn_quiz = Button(guiStart, text="Quiz", command=openQuiz)
btn_quiz.place(x=0, y=30)

mainloop()
