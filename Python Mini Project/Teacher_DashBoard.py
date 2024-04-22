from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, simpledialog
import sys
import os
from connection_provider import *

conn=getConn()
querryWritter=conn.cursor()
dbname=sys.argv[1]
quizName=sys.argv[2]
querryWritter.execute(f"use {dbname}")
try:
    if sys.argv[2]=="n":
        quizName=simpledialog.askstring("Input", "Please enter your Quiz-Name:")
        quizName=str(quizName).replace(" ","")
        querryWritter.execute(f"create table IF NOT EXISTS {quizName}(qno INTEGER PRIMARY KEY,question VARCHAR(60),op1 VARCHAR(60),op2 VARCHAR(60),op3 VARCHAR(60),op4 VARCHAR(60),answer VARCHAR(60))")
        querryWritter.execute(f"insert into {dbname}.quizname values(%s)",(quizName,))

        conn.commit()
except:
    pass
def image_2_clicked(event):
    # print("display")
    os.system(f"python teacher_display_ques.py {dbname} {quizName}")

def image_3_clicked(event):
    # print("delete")
    os.system(f"python teacher_delete_question.py {dbname} {quizName}")

def image_4_clicked(event):
    # print("update")
    os.system(f"python teacher_update_question.py {dbname} {quizName}")

def image_5_clicked(event):
    os.system(f"python teacher_add_new_question.py {dbname} {quizName}")
def image_6_clicked(event):
    os.system(f"python teacher_display_result.py {dbname} {dbname+"_"+quizName+"_result"}") 
    pass

conn.commit()

window = Tk()

window.geometry("1200x700+270+190")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=("Images\\t_db_index1.png"))
image_1 = canvas.create_image(
    600.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("Images\\teacher_dashboard_display.png"))
image_2 = canvas.create_image(
    845.0,
    64.0,
    image=image_image_2
)
canvas.tag_bind(image_2, "<Button-1>", image_2_clicked)

image_image_3 = PhotoImage(
    file=("Images\\teacher_dashboard_result.png"))
image_3 = canvas.create_image(
    1051.0,
    64.0,
    image=image_image_3
)
canvas.tag_bind(image_3, "<Button-1>", image_6_clicked)

image_image_4 = PhotoImage(
    file=("Images\\teacher_dashboard_delete.png"))
image_4 = canvas.create_image(
    592.0,
    64.0,
    image=image_image_4
)
canvas.tag_bind(image_4, "<Button-1>", image_3_clicked)
#update
image_image_5 = PhotoImage(
    file=("Images\\teacher_dashboard_update.png"))
image_5 = canvas.create_image(
    342.0,
    64.0,
    image=image_image_5
)
canvas.tag_bind(image_5, "<Button-1>", image_4_clicked)

#add
image_image_6 = PhotoImage(
    file=("Images\\teacher_dashboard_add_new_question.png"))
image_6 = canvas.create_image(
    109.0,
    64.0,
    image=image_image_6
)
canvas.tag_bind(image_6, "<Button-1>", image_5_clicked)

window.resizable(False, False)
window.mainloop()
