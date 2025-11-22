import tkinter as tk
from PIL import Image, ImageTk

# Create window
window = tk.Tk()
window.config(background="green")
window.geometry("500x500")
window.title("Employee Form")

# Variables
id_var = tk.StringVar()
name_var = tk.StringVar()
sal_var = tk.StringVar()

# Function for Submit button
def submit():
    emp_id = id_var.get()
    emp_name = name_var.get()
    emp_sal = sal_var.get()
    
    print(f"ID: {emp_id}, Name: {emp_name}, Salary: {emp_sal}")
    

    import sqlite3
    # connected
    conn = sqlite3.connect('mynew.db')
    # add cursor
    c = conn.cursor()
    # create a table
    c.execute(" CREATE TABLE IF NOT EXISTS EMPLOYEES (ID INT,NAME VARCHAR(20),SALARY INT)")
    c.execute("INSERT INTO EMPLOYEES VALUES(?,?,?)",(emp_id,emp_name,emp_sal))
    # commit the changes
    conn.commit()   
    c.close()
    # close the connection
    conn.close()

    
    # Optional: Show in GUI too
    result_label.config(text=f"ID: {emp_id}\nName: {emp_name}\nSalary: {emp_sal}")

# Labels and Entry fields
tk.Label(window, text="Employee ID:", font=("Arial", 16), bg="green", fg="white").pack(pady=5)
tk.Entry(window, textvariable=id_var, font=("Arial", 14)).pack(pady=5)

tk.Label(window, text="Employee Name:", font=("Arial", 16), bg="green", fg="white").pack(pady=5)
tk.Entry(window, textvariable=name_var, font=("Arial", 14)).pack(pady=5)

tk.Label(window, text="Salary:", font=("Arial", 16), bg="green", fg="white").pack(pady=5)
tk.Entry(window, textvariable=sal_var, font=("Arial", 14)).pack(pady=5)

# Submit button
tk.Button(window, text="Submit", font=("Arial", 16), bg="blue", fg="white", command=submit).pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 14), bg="green", fg="yellow")
result_label.pack(pady=20)

# Run the window
window.mainloop()