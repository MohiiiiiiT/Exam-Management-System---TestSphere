from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import os
def on_image_click(event):
    print("Help2 image clicked")  # You can replace this with your desired action

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

image_image_1 = PhotoImage(file=("Images\\help1.png"))
canvas.create_image(600.0, 350.0, image=image_image_1)

image_image_2 = PhotoImage(file=("Images\\help2.png"))
image_2 = canvas.create_image(1034.0, 62.0, image=image_image_2)

# Function to handle click event on help2.png
def on_image_click(event):
    # print("Help2 image clicked")  # You can replace this with your desired action
    window.destroy()
    os.system("python main.py")

# Bind click event to help2.png
canvas.tag_bind(image_2, "<Button-1>", on_image_click)

window.resizable(False, False)
window.mainloop()
