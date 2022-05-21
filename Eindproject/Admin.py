import mysql.connector
from tkinter import *
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="fcsyntra"
)

mycursor = db.cursor()


def voeg_admin_toe():
    lijst_new_admin = [admin_vn_entry.get(), admin_an_entry.get(), admin_email_entry.get(), admin_pw_entry.get()]
    teller = 0
    for x in lijst_new_admin:
        if len(x) > 0:
            teller = teller + 1
    if teller < 4:
        messagebox.showinfo("", "U heeft niet alle verplichte velden ingevuld")
    elif teller == 4:
        sql = "INSERT INTO admin (voornaam, achternaam, email, paswoord) VALUES (%s,%s,%s,%s)"
        val = [admin_vn_entry.get(), admin_an_entry.get(), admin_email_entry.get(), admin_pw_entry.get()]
        mycursor.execute(sql, val)
        db.commit()
    return


def delete_reservation():
    lijst_delete1 = [vak_entry.get(), rij_entry.get(), stoel_entry.get()]
    d1_teller = 0
    for x in lijst_delete1:
        if len(x) > 0:
            d1_teller = d1_teller + 1
    if d1_teller < 3:
        messagebox.showinfo("", "Gelieve vak, rij en stoelnummer in te vullen")
    elif d1_teller == 3:
        v = str(lijst_delete1[0])
        r = str(lijst_delete1[1])
        s = str(lijst_delete1[2])
        sql = "UPDATE stadion SET reserved = 'Nee' WHERE (tribune = %s AND rij = %s AND stoel = %s)"
        val = (v, r, s)
        mycursor.execute(sql, val)
        db.commit()
    return


def delete_all_reservations():
    sql = "UPDATE stadion SET reserved = 'Nee'"
    mycursor.execute(sql)
    db.commit()
    return


admin_page = Tk()
admin_page.title("FC Syntra Genk")
admin_page.state("zoomed")
admin_page.config(bg='DodgerBlue3')
admin_page.grid_rowconfigure(0, weight=1)
admin_page.grid_columnconfigure(0, weight=1)

# TITLE PAGE
L_Title = Label(admin_page, text="FC Syntra - Admin", fg='White', bg='DodgerBlue3', font=('Helvetica', 40))
L_Title.pack(pady=20)

"""
# LOGO
my_logo = Image.open("syntrapxl_academie_logo_digitaal_rgb_square.png")
resized = my_logo.resize((400, 400), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized)
new_logo_label = Label(admin_page, image=new_logo, bg="DodgerBlue3")
new_logo_label.place(x=1510, y=45)
"""

# CANVAS
# CANVAS: kader voor lijnen
my_canvas = Canvas(admin_page, width=1224, height=800, background="DodgerBlue2", highlightthickness=0)
my_canvas.grid_rowconfigure(0, weight=1)
my_canvas.grid_columnconfigure(0, weight=1)
my_canvas.pack(padx=5, pady=90)

"""
# CANVAS: lijnen in het kader met beginpunt x-as, beginpunt y-as, eindpunt y-as,lengte, kleur, breedte
my_canvas.create_line(1224, 0, 400, 250, fill="white", width=8)
my_canvas.create_line(1224, 0, 400, 400, fill="SteelBlue2", width=8)
my_canvas.create_line(1224, 0, 400, 600, fill="RoyalBlue4", width=8)
"""

# LABELS

title_all = Label(text="ENKELE RESERVATIE", bg="DodgerBlue2", fg="White", font=('Helvetica', 20, "bold"))
title_all.place(x=270, y=210)

vak = Label(text="Vak", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
vak.place(x=270, y=260)

rij = Label(text="Rij", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
rij.place(x=270, y=310)

stoel = Label(text="Stoel nummer", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
stoel.place(x=268, y=360)

title_all = Label(text="ALLE RESERVATIES", bg="DodgerBlue2", fg="White", font=('Helvetica', 20, "bold"))
title_all.place(x=270, y=510)

title_all = Label(text="NIEUWE ADMIN", bg="DodgerBlue2", fg="White", font=('Helvetica', 20, "bold"))
title_all.place(x=900, y=210)

admin_vn = Label(text="Voornaam", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_vn.place(x=900, y=260)

admin_an = Label(text="Achternaam", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_an.place(x=900, y=310)

admin_email = Label(text="Email", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_email.place(x=900, y=360)

admin_pw = Label(text="Paswoord", bg="DodgerBlue2", fg="White", font=('Helvetica', 12))
admin_pw.place(x=900, y=410)

# TEKSTVAKKEN
vak = StringVar
rij = StringVar
stoel = StringVar
voornaam = StringVar
achternaam = StringVar
email = StringVar
paswoord = StringVar

vak_entry = Entry(width=10, highlightthickness=2)
vak_entry.place(x=400, y=260, height=30)

rij_entry = Entry(width=10, highlightthickness=2)
rij_entry.place(x=400, y=310, height=30)

stoel_entry = Entry(width=10, highlightthickness=2)
stoel_entry.place(x=400, y=360, height=30)

admin_vn_entry = Entry(width=20, highlightthickness=2)
admin_vn_entry.place(x=1200, y=260, height=30)

admin_an_entry = Entry(width=20, highlightthickness=2)
admin_an_entry.place(x=1200, y=310, height=30)

admin_email_entry = Entry(width=20, highlightthickness=2)
admin_email_entry.place(x=1200, y=360, height=30)

admin_pw_entry = Entry(width=20, highlightthickness=2)
admin_pw_entry.place(x=1200, y=410, height=30)

# BUTTON CONNECT
delete_button1 = Button(text="Verwijder reservatie", width="30", command=delete_reservation, bg="White")
delete_button1.place(x=270, y=410, height="30")

delete_button2 = Button(text="Verwijder alle reservaties", width="30", command=delete_all_reservations,
                        bg="White")
delete_button2.place(x=270, y=560, height="30")

add_button = Button(text="Voeg admin toe", width="30", command=voeg_admin_toe, bg="White")
add_button.place(x=900, y=510, height="30")

admin_page.mainloop()
