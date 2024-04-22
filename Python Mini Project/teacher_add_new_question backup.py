from tkinter import *
from connection_provider import *
import sys
import os

conn=getConn()
querryWritter=conn.cursor()
dbName="PratikShah_T020"
quizName="q1"
# dbName=sys.argv[1]
# quizName=sys.argv[2]
querryWritter.execute(f"USE {dbName}")

def image_3_clicked(event=None):
    entry_1_value = entry_1.get()
    entry_2_value = entry_2.get()
    entry_3_value = entry_3.get()
    entry_4_value = entry_4.get()
    entry_5_value = entry_5.get()
    entry_6_value = entry_6.get()
    selected_value = selected_option.get()
    if selected_value == 1:
        selected_value = entry_3_value
    elif selected_value == 2:
        selected_value = entry_4_value
    elif selected_value == 3:
        selected_value = entry_5_value
    elif selected_value == 4:
        selected_value = entry_6_value

    print("Entry 1 value:", entry_1_value)
    print("Entry 2 value:", entry_2_value)
    print("Entry 3 value:", entry_3_value)
    print("Entry 4 value:", entry_4_value)
    print("Entry 5 value:", entry_5_value)
    print("Entry 6 value:", entry_6_value)
    print("Selected option:", selected_value)   

def image_2_clicked(event=None):
    window.destroy()


# Create a window without the title bar and borders
window = Tk()
window.geometry("950x505")
window.configure(bg="#FFFFFF")
window.overrideredirect(True)  # Removes the title bar and borders
window.attributes('-topmost', True)  # Keep the window on top

# Calculate the position to center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - 950) // 2
y_coordinate = (screen_height - 505) // 2
window.geometry(f"+{x_coordinate+25}+{y_coordinate+75}")

window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=505,
    width=950,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    950.0,
    505.0,
    fill="#F0F0F0",
    outline=""
)

image_image_1 = PhotoImage(file=("Images\\addques1.png"))
canvas.create_image(175.0, 192.0, image=image_image_1)

image_image_2 = PhotoImage(file=("Images\\addques2.png"))
image_2 = canvas.create_image(879.0, 47.0, image=image_image_2)
canvas.tag_bind(image_2, "<Button-1>", image_2_clicked)

entry_frame_1 = Frame(window, bd=1, relief="solid")
entry_frame_1.place(x=278.0, y=31.0, width=300.0, height=30.0)
entry_1 = Entry(entry_frame_1, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.pack(fill="both", expand=True)
entry_1.insert(0,"1")
entry_1.config(state="readonly")

entry_frame_2 = Frame(window, bd=1, relief="solid")
entry_frame_2.place(x=278.0, y=112.0, width=570.0, height=30.0)
entry_2 = Entry(entry_frame_2, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.pack(fill="both", expand=True)

entry_frame_3 = Frame(window, bd=1, relief="solid")
entry_frame_3.place(x=278.0, y=170.0, width=570.0, height=30.0)
entry_3 = Entry(entry_frame_3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_3.pack(fill="both", expand=True)

entry_frame_4 = Frame(window, bd=1, relief="solid")
entry_frame_4.place(x=278.0, y=222.0, width=570.0, height=30.0)
entry_4 = Entry(entry_frame_4, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_4.pack(fill="both", expand=True)

entry_frame_5 = Frame(window, bd=1, relief="solid")
entry_frame_5.place(x=278.0, y=273.0, width=570.0, height=30.0)
entry_5 = Entry(entry_frame_5, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_5.pack(fill="both", expand=True)

entry_frame_6 = Frame(window, bd=1, relief="solid")
entry_frame_6.place(x=278.0, y=323.0, width=570.0, height=30.0)
entry_6 = Entry(entry_frame_6, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_6.pack(fill="both", expand=True)

image_image_3 = PhotoImage(file=("Images\\addques3.png"))
image_3 = canvas.create_image(210.0, 427.0, image=image_image_3)

canvas.tag_bind(image_3, "<Button-1>", image_3_clicked)

Label(window,bd=0, fg="#FF0000", font=("Inter", 24),text="Select Correct Answer").place(x=613.0, y=392.0, anchor="nw")

selected_option = IntVar()

radio_button_4 = Radiobutton(window, variable=selected_option, value=1)
radio_button_4.place(x=242.0, y=170.0)  # Adjusted y-coordinate to align with entry_3

radio_button_5 = Radiobutton(window, variable=selected_option, value=2)
radio_button_5.place(x=242.0, y=220.0)  # Adjusted y-coordinate to align with entry_4

radio_button_6 = Radiobutton(window, variable=selected_option, value=3)
radio_button_6.place(x=242.0, y=270.0)  # Adjusted y-coordinate to align with entry_5

radio_button_7 = Radiobutton(window, variable=selected_option, value=4)
radio_button_7.place(x=242.0, y=320.0)  # Adjusted y-coordinate to align with entry_6

window.resizable(False, False)
window.mainloop()
