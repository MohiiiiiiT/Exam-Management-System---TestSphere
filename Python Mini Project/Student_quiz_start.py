from tkinter import Radiobutton, IntVar
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from connection_provider import *
import sys
import os
class StaticVariables:
    q_No=1
    results=[]
    marks=0
    is_not_rep=[]
    is_correct=[]
    finalList=[]

db_name=sys.argv[1]
tb_name=sys.argv[2]
# db_name="SiddheshMasurkar_T001"
tb_name=sys.argv[2]

stud_username=sys.argv[3]

conn=getConn()
querryWritter=conn.cursor()
answer=""
question_length=0

def getAnswer():
    answer1=selected_option.get()
    if answer1==1:
        answer1=getText(opt1_label)
    elif answer1==2:
        answer1=getText(opt2_label)
    elif answer1==3:
        answer1=getText(opt3_label)
    elif answer1==4:
        answer1=getText(opt4_label)
    return answer1

def getQues():
    canvas.itemconfigure(image_4, state='normal')
    if StaticVariables.q_No==1:
        canvas.itemconfigure(image_4, state='hidden')
    querry=f"select * from {db_name}.{tb_name}"
    querryWritter.execute(querry)
    len_of_ques=len(querryWritter.fetchall())
    q_No=StaticVariables.q_No
    querry=f"select * from {db_name}.{tb_name} where qno=%s"
    querryWritter.execute(querry,(q_No,))
    result=querryWritter.fetchone()
    setText(ques_no_label,int(result[0]))
    setText(sample_ques_label,result[1])
    setText(opt1_label,result[2])
    setText(opt2_label,result[3])
    setText(opt3_label,result[4])
    setText(opt4_label,result[5])
    if len_of_ques==q_No:   # To hide the next button 
        canvas.itemconfigure(image_3, state='hidden')
        return
    canvas.itemconfigure(image_3, state='normal')

    # answer=result[6]
    # print(result)
    StaticVariables.results=list(result)
def on_next_click(event):
    select_opt = getAnswer()
    try:
        # Attempt to insert or update the user's answer
        querry = f"insert into {stud_username}.{db_name + '_' + tb_name} values (%s, %s, %s, %s)"
        querryWritter.execute(querry, (StaticVariables.q_No, StaticVariables.results[1], select_opt, StaticVariables.results[-1]))
        conn.commit()
    except:
        # If insertion fails, attempt to update the selected answer
        querry = f"update {stud_username}.{db_name + '_' + tb_name} set question=%s, correct_answer=%s, selected_answer = %s where q_no = %s"

        querryWritter.execute(querry, (StaticVariables.results[1],StaticVariables.results[-1],select_opt, StaticVariables.q_No))
    
    # Check the selected answer against the correct answer and update marks accordingly
    if select_opt == StaticVariables.results[-1] and StaticVariables.is_not_rep[StaticVariables.q_No - 1]:
        StaticVariables.marks += 1
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
        StaticVariables.is_correct[StaticVariables.q_No - 1] = True
    elif StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and not StaticVariables.is_correct[StaticVariables.q_No - 1]:
        StaticVariables.marks += 1
        StaticVariables.is_correct[StaticVariables.q_No - 1] = True
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
    elif (StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt != StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]) or \
         (not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]) or \
         (not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]) or \
         (StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt != StaticVariables.results[-1] and not StaticVariables.is_correct[StaticVariables.q_No - 1]):
        pass
    elif not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt == StaticVariables.results[-1] and not StaticVariables.is_correct[StaticVariables.q_No - 1]:
        StaticVariables.marks += 1
        StaticVariables.is_correct[StaticVariables.q_No - 1] = True
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
    elif not StaticVariables.is_not_rep[StaticVariables.q_No - 1] and select_opt != StaticVariables.results[-1] and StaticVariables.is_correct[StaticVariables.q_No - 1]:
        StaticVariables.marks -= 1
        StaticVariables.is_correct[StaticVariables.q_No - 1] = False
        StaticVariables.is_not_rep[StaticVariables.q_No - 1] = False
    conn.commit()
    # print("next", (StaticVariables.results[-1] == select_opt))
    if StaticVariables.q_No==int(getText(total_ques_label))-1:
        # print(StaticVariables.results)
        StaticVariables.finalList=[]
        querry=f"select * from {db_name}.{tb_name} where qno=%s"
        querryWritter.execute(querry,(int(getText(total_ques_label)),))
        StaticVariables.finalList=list(querryWritter.fetchone())
        pass
    StaticVariables.results.clear()
    StaticVariables.q_No += 1
    getQues()

def on_prev_click(event):
    StaticVariables.q_No-=1
    getQues()
    # print("prev")

def quizStart():
    querryWritter.execute(f"use {stud_username}")
    querryWritter.execute(f"Create table if not exists {db_name+"_"+tb_name}(q_no integer primary key,question varchar(80),selected_answer varchar(80),correct_answer varchar(80))")
    querry=f"select * from {db_name}.{tb_name}"
    querryWritter.execute(querry)
    len_of_ques=len(querryWritter.fetchall())
    setText(total_ques_label,len_of_ques)
    for i in range(len_of_ques):
         StaticVariables.is_not_rep.append(True)
         StaticVariables.is_correct.append(False)
    conn.commit()
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


def on_image_2_click(event):        # Actually used for submit
    if StaticVariables.q_No==int(getText(total_ques_label)):
            select_opt = getAnswer()
            # print(StaticVariables.finalList)
            # print(StaticVariables.results)
            try:
                
                # Attempt to insert or update the user's answer
                querry = f"insert into {stud_username}.{db_name + '_' + tb_name} values (%s, %s, %s, %s)"
                querryWritter.execute(querry, (getText(ques_no_label), getText(sample_ques_label), select_opt, StaticVariables.finalList[-1]))
                conn.commit()
            except:
                # If insertion fails, attempt to update the selected answer
                querry = f"update {stud_username}.{db_name + '_' + tb_name} set question=%s, correct_answer=%s, selected_answer = %s where q_no = %s"
                querryWritter.execute(querry, (StaticVariables.finalList[1],StaticVariables.finalList[-1],select_opt, StaticVariables.q_No))
            # klasdf
            if select_opt==StaticVariables.finalList[-1]:
                # print("True Answer last")
                StaticVariables.marks+=1
            else:
                pass
                # print("False Answer last")
            conn.commit()
            # print("next", (StaticVariables.finalList[-1] == select_opt))
            querryWritter.execute(f"use {db_name}")
            querry = f"CREATE TABLE IF NOT EXISTS {db_name + '_' + tb_name}_result (stud_username VARCHAR(80), marks INTEGER, total_questions INTEGER)"
            querryWritter.execute(querry)
            querry=f"select * from {db_name}.{tb_name}"
            querryWritter.execute(querry)
            len_of_ques=len(querryWritter.fetchall())
            querry=f"insert into {db_name + '_' + tb_name}_result values(%s,%s,%s)"
            querryWritter.execute(querry,(stud_username,StaticVariables.marks,len_of_ques))
            conn.commit()
            StaticVariables.results.clear()
            # print("Answer is",getAnswer())
            window.destroy()
            os.system(f"python student_score.py {db_name} {tb_name} {stud_username} {len_of_ques}")
            return

    select_opt = getAnswer()
    # print(StaticVariables.results)
    # print(StaticVariables.results)
    try:
        
        # Attempt to insert or update the user's answer
        querry = f"insert into {stud_username}.{db_name + '_' + tb_name} values (%s, %s, %s, %s)"
        querryWritter.execute(querry, (getText(ques_no_label), getText(sample_ques_label), select_opt, StaticVariables.results[-1]))
        conn.commit()
    except:
        # If insertion fails, attempt to update the selected answer
        querry = f"update {stud_username}.{db_name + '_' + tb_name} set question=%s, correct_answer=%s, selected_answer = %s where q_no = %s"
        querryWritter.execute(querry, (StaticVariables.results[1],StaticVariables.results[-1],select_opt, StaticVariables.q_No))
    # klasdf
    if select_opt==StaticVariables.results[-1]:
        # print("True Answer last")
        StaticVariables.marks+=1
    else:
        # print("False Answer last")
        pass
    conn.commit()
    # print("next", (StaticVariables.results[-1] == select_opt))
    querryWritter.execute(f"use {db_name}")
    querry = f"CREATE TABLE IF NOT EXISTS {db_name + '_' + tb_name}_result (stud_username VARCHAR(80), marks INTEGER, total_questions INTEGER)"
    querryWritter.execute(querry)
    querry=f"select * from {db_name}.{tb_name}"
    querryWritter.execute(querry)
    len_of_ques=len(querryWritter.fetchall())
    querry=f"insert into {db_name + '_' + tb_name}_result values(%s,%s,%s)"
    querryWritter.execute(querry,(stud_username,StaticVariables.marks,len_of_ques))
    conn.commit()
    StaticVariables.results.clear()
    # print("Answer is",getAnswer())
    window.destroy()
    os.system(f"python student_score.py {db_name} {tb_name} {stud_username} {len_of_ques}")

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
