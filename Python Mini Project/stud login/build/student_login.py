from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\python\GUI\Python Mini Project\stud login\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    print("Entry 1:", value_1)
    print("Entry 2:", value_2)


# Bind click event to image2
canvas.tag_bind(image_2, "<Button-1>", on_image_2_click)

window.resizable(False, False)
window.mainloop()
