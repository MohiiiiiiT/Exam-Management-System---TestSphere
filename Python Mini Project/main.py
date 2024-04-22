from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
window = Tk()

window.geometry("1219x700")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1219,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file="Images\\index_bg.png")
image_1 = canvas.create_image(
    609.0,
    350.0,
    image=image_image_1
)

def openStudent():
    window.destroy()
    os.system("python student_login.py")

button_image_1 = PhotoImage(
    file="Images\\index_stud_btn.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=openStudent,
    relief="flat"
)

button_1.place(
    x=483.0,
    y=37.0,
    width=146.51162719726562,
    height=42.0
)
button_image_2 = PhotoImage(
    file="Images\\index_help_btn.png")
def openHelp():
    window.destroy()
    os.system("python help.py")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=openHelp,
    relief="flat"
)

button_2.place(
    x=1019.0,
    y=36.0,
    width=146.0869598388672,
    height=42.0
)
button_image_3 = PhotoImage(
    file="Images\\index_teacher_btn.png")
def openTeacherLogin():
    window.destroy()
    os.system("python teacher_sign_in.py")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=openTeacherLogin,
    relief="flat"
)

button_3.place(
    x=662.0,
    y=37.0,
    width=146.0869598388672,
    height=42.0
)
button_image_4 = PhotoImage(
    file="Images\\index_admin_btn.png")
def openAdmin():
    window.destroy()
    os.system("python admin_index.py")
    pass
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=openAdmin,
    relief="flat"
)
button_4.place(
    x=841.0,
    y=37.0,
    width=146.0869598388672,
    height=42.0
)
window.resizable(False, False)
window.mainloop()
