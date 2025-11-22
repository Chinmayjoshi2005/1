# Tkinter Registration Form 

import tkinter as Chinu
import sqlite3
from tkinter import messagebox

# ---------- Window Setup ----------

window = Chinu.Tk()
window.title("Registration Form")
window.geometry("800x600")
window.config(background="White")

# ---------- Heading ----------

label = Chinu.Label(window, text="Registration Form", font=("Arial", 30),bg='sky blue', fg="Black", width=20)
label.place(x=180, y=50)

# ---------- NAME ----------

name = Chinu.Label(window, text='Name', font=('Arial', 20), bg='white', fg="Black")
name.place(x=100, y=150)
name_entry = Chinu.Entry(window, font=('Arial', 18), bg='lightgrey', fg="Black")
name_entry.place(x=280, y=150)

# ---------- EMAIL ----------

email = Chinu.Label(window, text='Email', font=('Arial', 20), bg='white', fg="Black")
email.place(x=100, y=200)
email_entry = Chinu.Entry(window, font=('Arial', 18), bg='lightgrey', fg="Black")
email_entry.place(x=280, y=200)

# ---------- MOBILE ----------

mob = Chinu.Label(window, text='Mobile', font=('Arial', 20), bg='white', fg="Black")
mob.place(x=100, y=250)
mob_entry = Chinu.Entry(window, font=('Arial', 18), bg='lightgrey', fg="Black")
mob_entry.place(x=280, y=250)

# ---------- Submit Function ----------

def submit(event=None):
    get_name = name_entry.get()
    get_email = email_entry.get()
    get_mob = mob_entry.get()

    # Simple validation
    if get_name == "" or get_email == "" or get_mob == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    # Database connection
    conn = sqlite3.connect('Quentity.db')
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT,
        EMAIL TEXT,
        MOBILE TEXT
    )
    """)

    c.execute("INSERT INTO EMPLOYEES (NAME, EMAIL, MOBILE) VALUES (?, ?, ?)",
              (get_name, get_email, get_mob))

    conn.commit()
    c.close()
    conn.close()

    # Success message
    messagebox.showinfo("Submission Successful", "Data has been submitted successfully!")

    # Clear input fields
    name_entry.delete(0, Chinu.END)
    email_entry.delete(0, Chinu.END)
    mob_entry.delete(0, Chinu.END)

    window.destroy()

# ---------- Submit Button ----------

submit_button = Chinu.Button(window, text="Submit",font=('Arial', 22), bg='Orange', fg='black')
submit_button.place(x=320, y=350)

# ---------- Bind Events ----------

submit_button.bind("<Button-1>", submit)

# ---------- Main Loop ----------

window.mainloop()