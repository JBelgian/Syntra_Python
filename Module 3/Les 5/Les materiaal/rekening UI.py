from tkinter import *
class Rekening:
    def __init__(self,id,zichtrekening,spaarrekening):
        self.id = id
        self.zichtrekening = zichtrekening
        self.spaarrekening = spaarrekening
    def totaal(self):
        return self.zichtrekening+self.spaarrekening



r = Rekening("R220001",5000,9000)
r.spaarrekening = 7000


window = Tk()
window.geometry("500x250")
window.title("Rekening")


var_id =StringVar()
var_zr =StringVar()
var_sr =StringVar()


def verander_id():
    r.id = txt_wijzig_id.get()
    print(r.id)
    var_id.set(r.id)

def verander_zichtrekening():
    r.zichtrekening = int(txt_wijzig_zichtrekening.get())
    euro_zr = "€"+str(r.zichtrekening)
    var_zr.set(euro_zr)
    print(r.zichtrekening)

def verander_spaarrekening():
    r.spaarrekening = int(txt_wijzig_spaarrekening.get())
    euro_sp = "€"+str(r.spaarrekening)
    var_sr.set(euro_sp)


var_id.set(r.id)
euro_zr = "€"+str(r.zichtrekening)
var_zr.set(euro_zr)
euro_sp = "€"+str(r.spaarrekening)
var_sr.set(euro_sp)

label_id = Label(window,text="ID").grid(row=0,column=0)
label_toon_id = Label(window,text=r.id,textvariable=var_id).grid(row=0,column=1)
txt_wijzig_id = Entry(window)
txt_wijzig_id.grid(row=0,column=2)
btn_wijzig_id = Button(window,text="Wijzig ID",command=verander_id)
btn_wijzig_id.grid(row=0,column=3)


label_zichtrekening = Label(window,text="Zichtrekening").grid(row=1,column=0)
label_toon_zichtrekening = Label(window,text="€ "+str(r.zichtrekening), textvariable=var_zr)
label_toon_zichtrekening.grid(row=1,column =1)
txt_wijzig_zichtrekening = Entry(window)
txt_wijzig_zichtrekening.grid(row=1,column=2)
btn_wijzig_zichtrekening = Button(window,text="Wijzig Zichtrekening",command = verander_zichtrekening)
btn_wijzig_zichtrekening.grid(row=1,column=3)

label_spaarrekening = Label(window,text="Spaarrekening").grid(row=2,column=0)
label_toon_spaarrekening = Label(window,text="€ "+str(r.spaarrekening), textvariable=var_sr)
label_toon_spaarrekening.grid(row = 2, column = 1)
txt_wijzig_spaarrekening = Entry(window)
txt_wijzig_spaarrekening.grid(row=2,column=2)
btn_wijzig_spaarrekening = Button(window,text="Wijzig Spaarrekening",command=verander_spaarrekening)
btn_wijzig_spaarrekening.grid(row=2,column=3)

label_totaal = Label(window,text="Totaal").grid(row=3,column=0)
label_toon_totaal = Label(window,text="€ "+str(r.totaal())).grid(row=3,column=1)


window.mainloop()
