from pathlib import Path
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from connection_provider import *
import os
conn=getConn()
queryWritter=conn.cursor()

def on_image_2_click(event):
    window.destroy()
    os.system(f"python Student_quiz_start_result.py {db_name} {tb_name} {stud_username}")
# db_name="PratikShah_T020"
# tb_name="q1"
# stud_username="MayureshKajale_A020"

db_name=sys.argv[1]
tb_name=sys.argv[2]
stud_username=sys.argv[3]
out_of=sys.argv[4]
score_table_name=db_name+"_"+tb_name+"_result"
querry=f"select * from {db_name}.{score_table_name} where stud_username=%s"
queryWritter.execute(querry, (stud_username,))
result=queryWritter.fetchone()
my_marks=result[1]
out_of=result[2]
# my_marks=2134
# out_of=23
window = Tk()

window.geometry("884x555")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 555,
    width = 884,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=("Images\\view_score_student_outof.png"))
image_1 = canvas.create_image(
    442.0,
    277.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("Images\\view_score_student_outof1.png"))
image_2 = canvas.create_image(
    440.0,
    410.0,
    image=image_image_2
)


canvas.tag_bind(image_2, "<Button-1>", on_image_2_click)
canvas.create_text(
    432.0,
    195.0,
    anchor="nw",
    text=my_marks,
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    432.0,
    264.0,
    anchor="nw",
    text=out_of,
    fill="#000000",
    font=("Inter", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
