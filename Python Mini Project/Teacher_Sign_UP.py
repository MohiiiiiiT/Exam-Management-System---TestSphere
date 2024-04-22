import tkinter as tk
from tkinter import Entry, PhotoImage, Canvas, messagebox
from connection_provider import getConn

conn = getConn()
queryWriter = conn.cursor()

def on_image_click(event):
    adminPassword = entry_5.get()
    teacherID = entry_1.get()
    fullName = entry_2.get()
    fn=fullName
    makePassword = entry_3.get()
    confirmPassword = entry_4.get()
    if adminPassword == "pass@123" and " " not in teacherID:
        if makePassword == confirmPassword:
            query = "INSERT INTO qemspython.teacherrecord VALUES (%s,%s, %s, %s)"
            fullName = fullName.replace(" ", "")
            queryWriter.execute(query, (teacherID,fn, (fullName + "_" + str(teacherID)), makePassword))
            conn.commit()
            dbName = fullName + "_" + str(teacherID)
            queryWriter.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")
            queryWriter.execute(f"CREATE TABLE IF NOT EXISTS {dbName}.quizName(quiz_name varchar(50))")
            conn.commit()
            messagebox.showinfo("", f"Your UserName is {fullName}_{teacherID} and Password is {makePassword}")
            window.destroy()
        else:
            messagebox.showerror("Error", "Your Password doesn't Match with Confirm Password")
    else:
        messagebox.showerror("Error", "Some Error Occurred")

window = tk.Tk()

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window width and height
window_width = 751
window_height = 455

# Calculate position for centering the window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window position
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=window_height,
    width=window_width,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file="Images\\Teacher_signup_login.png")
canvas.create_image(window_width // 2, window_height // 2, image=image_image_1)

image_image_2 = PhotoImage(file="Images\\teacher_signup_submit.png")
image_2 = canvas.create_image(404.0, 360.0, image=image_image_2)

entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=398.0, y=98.0, width=231.0, height=24.0)

entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=398.0, y=145.0, width=231.0, height=24.0)

entry_3 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.place(x=398.0, y=192.0, width=231.0, height=24.0)

entry_4 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_4.place(x=398.0, y=239.0, width=231.0, height=24.0)

entry_5 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_5.place(x=398.0, y=285.0, width=231.0, height=24.0)

canvas.tag_bind(image_2, "<Button-1>", on_image_click)

window.resizable(False, False)
window.mainloop()
