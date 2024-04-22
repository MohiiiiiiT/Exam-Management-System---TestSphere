from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import os

def on_image_2_click(event):
    os.system("python Student_Sign_UP.py")

def on_image_3_click(event):
    os.system("python Teacher_Sign_UP.py")

window = Tk()

window.geometry("1200x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=("Images\\index_admin_bg.png"))
image_1 = canvas.create_image(
    600.0,
    350.0,
    image=image_image_1
)
image_image_2 = PhotoImage(file=("Images\\admin_addstudent.png"))
image_2 = canvas.create_image(
    179.0,
    64.0,
    image=image_image_2
)

canvas.tag_bind(image_2, "<Button-1>", on_image_2_click)

image_image_3 = PhotoImage(file=("Images\\admin_addteacher.png"))
image_3 = canvas.create_image(
    483.0,
    64.0,
    image=image_image_3
)
canvas.tag_bind(image_3, "<Button-1>", on_image_3_click)

window.resizable(False, False)
window.mainloop()
