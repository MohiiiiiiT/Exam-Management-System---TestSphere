from tkinter import Radiobutton, IntVar
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from connection_provider import *
import sys
import os
class StaticVariables:
    q_No=1

# db_name="PratikShah_T020"
# tb_name="q1"
# stud_username="MayureshKajale_A020"
db_name=sys.argv[1]
tb_name=sys.argv[2]
stud_username=sys.argv[3]

conn=getConn()
querryWritter=conn.cursor()
answer=""
question_length=0
# stud_username="MayureshKajale_A020"
# db_name="pratikshah_t020"
# tb_name="q1"

def getAnswer():
    query = f"SELECT selected_answer FROM {stud_username}.{db_name + '_' + tb_name} WHERE q_no = %s"
    querryWritter.execute(query, (StaticVariables.q_No,))
    result = querryWritter.fetchone()
    if result:
        return result[0]
    else:
        return ""
def getQues():
    canvas.itemconfigure(image_4, state='normal')
    if StaticVariables.q_No == 1:
        canvas.itemconfigure(image_4, state='hidden')
    
    query = f"SELECT * FROM {db_name}.{tb_name} WHERE qno = %s"
    querryWritter.execute(query, (StaticVariables.q_No,))
    result = querryWritter.fetchone()
    
    setText(ques_no_label, int(result[0]))
    setText(sample_ques_label, result[1])
    setText(opt1_label, result[2])
    setText(opt2_label, result[3])
    setText(opt3_label, result[4])
    setText(opt4_label, result[5])
    
    # Preselect the option stored in the selected_answer column
    selected_option_value = getAnswer()
    if selected_option_value:
        for i, opt_label in enumerate([opt1_label, opt2_label, opt3_label, opt4_label], start=1):
            if getText(opt_label) == selected_option_value:
                selected_option.set(i)
                break
    
    # Highlight the text corresponding to the correct_answer column
    correct_answer = result[6]  # Assuming correct answer is stored in the answer column
    for opt_label in [opt1_label, opt2_label, opt3_label, opt4_label]:
        if getText(opt_label) == correct_answer:
            canvas.itemconfig(opt_label, fill="green")
        else:
            canvas.itemconfig(opt_label, fill="#000000")
    
    # Define and populate len_of_ques
    querryWritter.execute(f"SELECT COUNT(*) FROM {db_name}.{tb_name}")
    len_of_ques = querryWritter.fetchone()[0]
    
    if len_of_ques == StaticVariables.q_No:   # To hide the next button 
        canvas.itemconfigure(image_3, state='hidden')
        return
    canvas.itemconfigure(image_3, state='normal')

    # print(result)

    # print(result)

def on_next_click(event):
    select_opt = getAnswer()
    StaticVariables.q_No += 1
    getQues()

def on_prev_click(event):
    StaticVariables.q_No-=1
    getQues()

def quizStart():
    querry = f"SELECT * FROM {db_name}.{tb_name}"
    querryWritter.execute(querry)
    total_questions = len(querryWritter.fetchall())
    setText(total_ques_label, total_questions)
    getQues()
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


image_image_3 = PhotoImage(
    file=("Images\\student_quiz_start_next.png"))
image_3 = canvas.create_image(
    776.0,
    493.0,
    image=image_image_3
)
canvas.tag_bind(image_3, "<Button-1>", on_next_click)
image_image_4 = PhotoImage(
    file=("Images\\student_quiz_start_prev.png"))
image_4 = canvas.create_image(
    523.0,
    493.0,
    image=image_image_4
)
canvas.tag_bind(image_4, "<Button-1>", on_prev_click)
selected_option = IntVar()

radio_button_1 = Radiobutton(
    window,
    variable=selected_option,
    value=1,
    bd=0,
    state="disabled",
    highlightthickness=0,
    relief="flat"
)
radio_button_1.place(x=236, y=254)

radio_button_2 = Radiobutton(
    window,
    variable=selected_option,
    value=2,
    bd=0,
    state="disabled",
    highlightthickness=0,
    relief="flat"
)
radio_button_2.place(x=236, y=304)

radio_button_3 = Radiobutton(
    window,
    variable=selected_option,
    value=3,
    bd=0,
    state="disabled",
    highlightthickness=0,
    relief="flat"
)
radio_button_3.place(x=236, y=357)

radio_button_4 = Radiobutton(
    window,
    variable=selected_option,
    value=4,
    bd=0,
    state="disabled",
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
    705.0,
    38.0,
    anchor="nw",
    text="total_ques",
    fill="#000000",
    font=("Inter", 24 * -1)
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
quizStart()
window.resizable(False, False)
window.mainloop()
