from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from connection_provider import *
from mysql.connector import *
from tkinter import messagebox
import os
root=getConn()
querryWritter=root.cursor()

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
image_image_1 = PhotoImage(
    file=("Images\\stud_login_1_first.png"))
image_1 = canvas.create_image(
    600.0,
    350.0,
    image=image_image_1
)

entry_bg_1 = canvas.create_image(
    981.0,
    354.5
)
entry_1 = Entry(
    bd=2,  # Set border width to 2 for a visible stroke
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=875.0,
    y=339.0,
    width=212.0,
    height=29.0
)

entry_bg_2 = canvas.create_image(
    981.0,
    414.5
)

entry_2 = Entry(
    bd=2,
    bg="#FFFFFF",
    show="*",
    fg="#000716",
    highlightthickness=0
)

entry_2.place(
    x=875.0,
    y=399.0,
    width=212.0,
    height=29.0
)

image_image_2 = PhotoImage(
    file=("Images\\stud_login_btn_2_second.png"))
image_2 = canvas.create_image(
    903.0,
    512.0,
    image=image_image_2
)

def on_image_2_click(event):
    value_1 = entry_1.get()
    value_2 = entry_2.get()
    # value_1="MohitMadke_A025"
    # value_2="mohit@123"
    querry = "SELECT * FROM qemspython.studentrecord WHERE username=%s AND password=%s"
    querryWritter.execute(querry, (value_1, value_2))
    rows = querryWritter.fetchall()
    row_count = len(rows)
    if row_count < 1:
        messagebox.showerror("Warning", "Invalid Username or Password")
    else:
        messagebox.showinfo("Welcome", f"Welcome {value_1}")
        window.destroy()
        os.system(f"python Student_option_select.py {value_1}")
    querryWritter.close()
    root.close()




# Bind click event to image2
canvas.tag_bind(image_2, "<Button-1>", on_image_2_click)

window.resizable(False, False)
window.mainloop()
