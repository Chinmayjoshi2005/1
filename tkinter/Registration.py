# Tkinter Registration Form

import tkinter as Chinu
window=Chinu.Tk()
window.config(background="White")
window.geometry("800x700")

#sqlite3db
import sqlite3
conn = sqlite3.connect('registration.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name TEXT, email TEXT, mobile NUMBER)''')
conn.commit()

# ********************** Registration **************************

lable=Chinu.Label(window,text="Registration Form",font=("bold",30),bg='sky blue',fg="Black", width=20)
lable.place(x=200,y=50)

# ********************** NAME **************************

name = Chinu.Label(window,text = 'NAME', font=('Arial',25),bg='white',fg="Black")
name.place(x=100,y=150)
name_entry = Chinu.Entry(window, font=('Arial',21), bg='lightgrey', fg = 'black')
name_entry.place(x=250,y=150)

# ********************** Email **************************

email = Chinu.Label(window,text = 'E-mail', font=('Arial',25),bg='white',fg="Black")
email.place(x=100,y=200)
email_entry = Chinu.Entry(window, font=('Arial',21), bg='lightgrey', fg = 'black')
email_entry.place(x=250,y=200)

# ********************** mobile no. **************************

mob = Chinu.Label(window,text = 'Mobile No.', font=('Arial',25),bg='white',fg="Black")
mob.place(x=100,y=250)
mob_entry = Chinu.Entry(window, font=('Arial',21), bg='lightgrey', fg = 'black')
mob_entry.place(x=250,y=250)

# ********************** submit button **************************

submit_button = Chinu.Button(window, text="Submit", font=('Arial', 25), bg='Orange', fg='black')
submit_button.place(x=320, y=350)

# ********************** db **************************

def submit():
    name = name_entry.get()
    email = email_entry.get()
    mobile = mob_entry.get()
    
    c.execute("INSERT INTO users (name, email, mobile) VALUES (?, ?, ?)", (name, email, mobile))
    conn.commit()

window.mainloop()
