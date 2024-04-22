from pathlib import Path
from tkinter import Radiobutton, IntVar
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\python\GUI\Python Mini Project\stud quiz ques\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    file=("Images\\student_quiz_start1_indexbg.png"))
image_1 = canvas.create_image(
    442.0,
    277.0,
    image=image_image_1
)
def setText(label_variable, new_text):
    canvas.itemconfig(label_variable, text=new_text)

def getText(label_variable):
    return canvas.itemcget(label_variable, "text")

def on_image_2_click(event):
    select_val=selected_option.get()
    if select_val==1:
        select_val=getText(opt1_label)
    if select_val==2:
        select_val=getText(opt2_label)
    if select_val==3:
        select_val=getText(opt3_label)
    if select_val==4:
        select_val=getText(opt4_label)
    print("Answer is",select_val)

image_image_2 = PhotoImage(
    file=("Images\\student_quiz_start_submit.png"))
image_2 = canvas.create_image(
    116.0,
    492.0,
    image=image_image_2
)
canvas.tag_bind(image_2, "<Button-1>", on_image_2_click)
image_image_3 = PhotoImage(
    file=("Images\\student_quiz_start_next.png"))
image_3 = canvas.create_image(
    776.0,
    493.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=("Images\\student_quiz_start_prev.png"))
image_4 = canvas.create_image(
    523.0,
    493.0,
    image=image_image_4
)

selected_option = IntVar()

radio_button_1 = Radiobutton(
    window,
    variable=selected_option,
    value=1,
    bd=0,
    highlightthickness=0,
    relief="flat"
)
radio_button_1.place(x=236, y=254)

radio_button_2 = Radiobutton(
    window,
    variable=selected_option,
    value=2,
    bd=0,
    highlightthickness=0,
    relief="flat"
)
radio_button_2.place(x=236, y=304)

radio_button_3 = Radiobutton(
    window,
    variable=selected_option,
    value=3,
    bd=0,
    highlightthickness=0,
    relief="flat"
)
radio_button_3.place(x=236, y=357)

radio_button_4 = Radiobutton(
    window,
    variable=selected_option,
    value=4,
    bd=0,
    highlightthickness=0,
    relief="flat"
)
radio_button_4.place(x=236, y=410)



sample_ques_label = canvas.create_text(
    219.0,
    192.0,
    anchor="nw",
    text="Sample Ques",
    fill="#000000",
    font=("Inter", 24 * -1)
)

ques_no_label = canvas.create_text(
    254.0,
    145.0,
    anchor="nw",
    text="ques_no",
    fill="#000000",
    font=("Inter", 24 * -1)
)

total_ques_label = canvas.create_text(
    715.0,
    17.0,
    anchor="nw",
    text="total_ques",
    fill="#000000",
    font=("Inter", 24 * -1)
)

your_score_label = canvas.create_text(
    674.0,
    43.0,
    anchor="nw",
    text="your_score",
    fill="#000000",
    font=("Inter", 24 * -1)
)

incorrect_one_label = canvas.create_text(
    646.0,
    74.0,
    anchor="nw",
    text="incorrect_one",
    fill="#FF0000",
    font=("Inter", 24 * -1)
)

missed_one_label = canvas.create_text(
    626.0,
    99.0,
    anchor="nw",
    text="missed_one",
    fill="#000000",
    font=("Inter", 24 * -1)
)

image_image_9 = PhotoImage(
    file=("Images\\student_quiz_start_img2.png"))
image_9 = canvas.create_image(
    616.0,
    71.0,
    image=image_image_9
)


opt1_label = canvas.create_text(
    278.0,
    245.0,
    anchor="nw",
    text="Opt1",
    fill="#000000",
    font=("Inter", 24 * -1)
)

opt2_label = canvas.create_text(
    278.0,
    299.0,
    anchor="nw",
    text="Opt2",
    fill="#000000",
    font=("Inter", 24 * -1)
)

opt3_label = canvas.create_text(
    280.0,
    352.0,
    anchor="nw",
    text="Opt3",
    fill="#000000",
    font=("Inter", 24 * -1)
)

opt4_label = canvas.create_text(
    278.0,
    404.0,
    anchor="nw",
    text="Opt4",
    fill="#000000",
    font=("Inter", 24 * -1)
)

# These are user-def function used to set and get text from label kind of widget

# setText(missed_one_label,"New Text")      # Excellent Work Done
# print(getText(missed_one_label))          # Good I'm proud of You ;)
window.resizable(False, False)
window.mainloop()
