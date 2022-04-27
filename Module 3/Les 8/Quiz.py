# Python program to create a simple GUI
# Simple Quiz using Tkinter

# import alles van tkinter
from tkinter import *

# import messagebox als mb van tkinter
from tkinter import messagebox as mb

# import json om json file te gebruiken voor data
import json


# class om de components van de GUI te defineren
class Quiz:
    def __init__(self):

        # zet question number naar 0
        self.q_no = 0

        # functie voor het weergeven van de titel in titel balk en de vraag
        self.display_title()
        self.display_question()

        # opt_selected houd een int vast die correspondeert met het gekoze antwoord
        self.opt_selected = IntVar()

        # weergeeft radio buttons voor de antwoord opties
        self.opts = self.radio_buttons()

        # weergeeft de antwoord opties voor de huidige vraag
        self.display_options()

        # weergeeft de knoppen next en quit
        self.buttons()

        # berekent het aantal vragen in de quiz
        self.data_size = len(question)

        # houd score van juiste antwoorden bij
        self.correct = 0

    # functie berekent correct en niet correct antwoord en weergeeft een message box met resultaat
    def display_result(self):

        # berekent foute antwoorden
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # berekent percentage juist geantwoord
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # toont message box met resultaten
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    # functie checkt antwoord wanneer op next wordt geduwt
    def check_ans(self, q_no):

        # check of the geselecteerde antwoord juist is
        if self.opt_selected.get() == answer[q_no]:
            # als het juist is returned de functie true
            return True

    # functie checkt of the geselecteerd antwoord juist is voor de huidige vraag
    # indien juist telt hij +1 bij correct antwoord teller
    # en gaat hij naar de volgende vraag, tenzij het de laatste vraag is
    # dan opent de functie het resultaten message box
    def next_btn(self):

        # Checkt of het antwoord juist is
        if self.check_ans(self.q_no):
            # als het antwoord juist is +1 op correcte teller
            self.correct += 1

        # gaat naar volgende vraag
        self.q_no += 1

        # checkt als de huidige vraag overeenkomt met het totaal aantal vragen in de quiz
        if self.q_no == self.data_size:

            # als huidige vraag de laatste vraag is open het resultaat message box
            self.display_result()

            # sluit de quiz
            gui.destroy()
        else:
            # anders toont de functie de volgende vraag en antwoorden
            self.display_question()
            self.display_options()

    # deze functie toont de twee knoppen
    # en zorgt ervoor de bij het klikken op de knop de juiste functie aangeroepen wordt
    def buttons(self):

        # eerste knop is de next knop, roept de volgende vraag of resultaat op
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # plaatsing van de next knop in het screen
        next_button.place(x=350, y=380)

        # de knop is de quit knop om het programma af te sluiten
        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        # plaatsing van de quit knop in het screen
        quit_button.place(x=700, y=50)

    # deze functie zorgt ervoor de antwoorden bij de huidige vraag worden weergeven
    def display_options(self):
        val = 0

        # deselecting van de opties
        self.opt_selected.set(0)

        # looping voor het weergeven van de verschillende antwoord mogelijkheden bij iedere radio button
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # functie voor het aanroepen en weergeven van de vraag
    def display_question(self):

        # label properties (kleur, lettertijpe, grootte) en aanroepen vraag
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')

        # plaatsing van de vraag in het screen
        q_no.place(x=70, y=100)

    # functie om titel te weergeven
    def display_title(self):

        # titel label properties (kleur, lettertijpe, grootte)
        title = Label(gui, text="DAJ QUIZ",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # plaatsing van de titel in het screen
        title.place(x=0, y=2)

    # functie om de radio buttons te displayen
    def radio_buttons(self):

        # initieel een lege versie aangemaakt
        q_list = []

        # positie van de eerste knop
        y_pos = 150

        # antwoord opties aan de lijst toevoegen
        while len(q_list) < 4:
            # radio button properties
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            # toevoegen van de radio buttons aan de lijst
            q_list.append(radio_btn)

            # plaatsing van de buttons
            radio_btn.place(x=100, y=y_pos)

            # incrementeren op de y-as positie met 40
            y_pos += 40

        # lijst terug koppelen naar hoofd programma
        return q_list


# Creeert GUI Window
gui = Tk()

# zet de groote van GUI Window
gui.geometry("800x450")

# zet de titel van de GUI Window
gui.title("DAJ Quiz")

# haalt de data van de json file
with open('data.json') as f:
    data = json.load(f)

# zet de vraag, opties en juist antwoord
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# start het programma
def startquiz():
    gui.mainloop()
# END OF THE PROGRAM