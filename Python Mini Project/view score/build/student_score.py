from pathlib import Path
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# my_marks=sys.argv[1]
my_marks=123
# out_of=sys.argv[2]
out_of=4141412

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
    216.0,
    433.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("Images\\view_score_student_outof2.png"))
image_3 = canvas.create_image(
    555.0,
    433.0,
    image=image_image_3
)

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
