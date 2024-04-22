from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter.ttk import Combobox  # Import Combobox from tkinter.ttk
from pathlib import Path
import os
import sys
from connection_provider import *

conn=getConn()
querryWriter=conn.cursor()
try:
    db_name=sys.argv[1]
    print(db_name)
    querryWriter.execute(f"USE {db_name}")
except:
        db_name="PratikShah_T020"
        querryWriter.execute(f"USE {db_name}")
def on_image_2_click(event):
    val1=entry_1.get()
    window.destroy()
    os.system(f"python Teacher_DashBoard.py {db_name} {val1}")
def on_image_3_click(event):
    window.destroy()
    os.system(f"python Teacher_DashBoard.py {db_name} n")

window = Tk()
window.geometry("403x432")
window.configure(bg="#110C0C")

canvas = Canvas(
    window,
    bg="#110C0C",
    height=432,
    width=403,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=("Images\\teacher_choice_bg.png"))
image_1 = canvas.create_image(201.0, 216.0, image=image_image_1)

entry_bg_1 = canvas.create_image(201.5, 192.0)
querryWriter.execute(f"select distinct quiz_name from {db_name}.quizname")
combo_values =querryWriter.fetchall()

entry_1 = Combobox(
    window,
    values=combo_values,
    state="readonly",
    background="#FFFFFF",
    foreground="#000716",
)
entry_1.place(x=80.0, y=180.0, width=243.0, height=22.0)

image_image_2 = PhotoImage(file=("Images\\teacher_choice_proceed.png"))
image_2 = canvas.create_image(202.0, 274.0, image=image_image_2)
canvas.tag_bind(image_2, "<Button-1>", on_image_2_click)

image_image_3 = PhotoImage(file=("Images\\teacher_choice_create_quiz.png"))
image_3 = canvas.create_image(93.0, 29.0, image=image_image_3)
canvas.tag_bind(image_3, "<Button-1>", on_image_3_click)

window.resizable(False, False)
window.mainloop()
