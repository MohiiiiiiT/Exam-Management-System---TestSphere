from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import os
from connection_provider import getConn

conn = getConn()
queryWriter = conn.cursor()

window = Tk()

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 1200
window_height = 700

# Calculate position for centering the window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
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

image_image_1 = PhotoImage(file="Images\\teacher_login_main.png")
image_1 = canvas.create_image(600.0, 350.0, image=image_image_1)

entry_bg_1 = canvas.create_image(981.0, 354.5)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
)
entry_1.place(
    x=875.0,
    y=339.0,
    width=212.0,
    height=29.0
)

entry_bg_2 = canvas.create_image(981.0, 414.5)
entry_2 = Entry(
    bd=0,
    show="*",
    bg="#FFFFFF",
    fg="#000716",
)
entry_2.place(
    x=875.0,
    y=399.0,
    width=212.0,
    height=29.0
)

button_image_1 = PhotoImage(file="Images\\teacher_sign_up_main.png")
def callTeacherSignUP():
    os.system("python Teacher_Sign_UP.py")

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=callTeacherSignUP,
    relief="flat"
)
button_1.place(
    x=921.0,
    y=493.0,
    width=138.0,
    height=38.0
)

button_image_2 = PhotoImage(file="Images\\teacher_sign_in_main.png")
def callTeacherDashBoard():
    username = entry_1.get()
    username = username.strip()
    password = entry_2.get()
    password = password.strip()
    queryWriter.execute("select username,password from qemspython.teacherrecord where username=%s and password=%s", (username, password))
    if queryWriter.fetchone():
        window.destroy()
        os.system(f"python teacher_choice.py {username}")
    else:
        messagebox.showinfo("", "Invalid Username or Password")

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=callTeacherDashBoard,
    relief="flat"
)
button_2.place(
    x=753.0,
    y=493.0,
    width=138.0,
    height=38.0
)

window.resizable(False, False)
window.mainloop()
