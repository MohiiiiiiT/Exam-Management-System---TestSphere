from tkinter import Tk, Canvas, PhotoImage
from tkinter.ttk import Combobox
import mysql.connector
import os
import sys
studUsername=sys.argv[1]
def get_database_list():
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="qemspython"
    )
    cursor = connection.cursor()
    
    # Execute query to get list of databases
    cursor.execute("SELECT username FROM teacherrecord")
    databases = [row[0] for row in cursor.fetchall()]
    
    connection.close()
    
    return databases

def get_table_list(selected_database):
    # Connect to selected database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=selected_database
    )
    cursor = connection.cursor()
    # Execute query to get list of tables
    cursor.execute("SELECT quiz_name FROM quizname")
    tables = [row[0] for row in cursor.fetchall()]
    
    connection.close()
    return tables

def on_combobox1_select(event):
    selected_database = combobox1.get()
    table_list = get_table_list(selected_database)
    combobox2['values'] = table_list

def on_image2_click(event):
    selected_database = combobox1.get()
    selected_table = combobox2.get()
    print("Selected Database:", selected_database)
    print("Selected Table:", selected_table)
    os.system(f"python Student_quiz_start.py {selected_database} {selected_table} {studUsername}")
    

window = Tk()

window.geometry("482x323")
window.configure(bg="#110C0C")

canvas = Canvas(
    window,
    bg="#110C0C",
    height=323,
    width=482,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=("Images\\stud_opt1.png"))
image_1 = canvas.create_image(
    243.0,
    161.0,
    image=image_image_1
)

entry_bg_1 = canvas.create_rectangle(
    204.0,
    148.0,
    447.0,
    170.0,
    fill="#FFFFFF",
    outline="#000716"
)

# Get list of databases
database_list = get_database_list()

# ComboBox for selecting database
combobox1 = Combobox(window, values=database_list)
combobox1.place(
    x=204.0,
    y=95.0,  # Swapped position
    width=243.0,
    height=22.0
)
combobox1.bind("<<ComboboxSelected>>", on_combobox1_select)

entry_bg_2 = canvas.create_rectangle(
    204.0,
    95.0,
    447.0,
    117.0,
    fill="#FFFFFF",
    outline="#000716"
)

# Placeholder for combobox2, will be updated dynamically
combobox2 = Combobox(window)
combobox2.place(
    x=204.0,
    y=148.0,  # Swapped position
    width=243.0,
    height=22.0
)

image_image_2 = PhotoImage(file=("Images\\stud_opt2.png"))
image_2 = canvas.create_image(
    196.0,
    230.0,
    image=image_image_2
)

# Bind click event to image2
canvas.tag_bind(image_2, "<Button-1>", on_image2_click)

window.resizable(False, False)
window.mainloop()
