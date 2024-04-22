import mysql.connector
from tkinter import *
from tkinter import ttk
import sys

def fetch_data(dbName, quizName):
    # Connect to your MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=dbName
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Fetch data from your table
    cursor.execute(f"SELECT qno, question, op1, op2, op3, op4, answer FROM {quizName}")
    data = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    return data

def display_data(dbName, quizName):
    # Fetch data from the database
    data = fetch_data(dbName, quizName)

    # Create a new window
    window = Tk()
    window.geometry("950x505")
    window.configure(bg="#FFFFFF")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - 950) // 2
    y_coordinate = (screen_height - 505) // 2
    window.geometry(f"+{x_coordinate + 25}+{y_coordinate + 75}")

    window.configure(bg="#FFFFFF")

    # Create a frame to contain the Treeview widget and scrollbar
    frame = Frame(window)
    frame.place(x=0, y=0, width=950, height=505)

    # Create Treeview widget
    tree = ttk.Treeview(frame, columns=("Question No.", "Question", "Option 1", "Option 2", "Option 3", "Option 4", "Answer"), show="headings")
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Add columns
    tree.heading("Question No.", text="Question No.")
    tree.heading("Question", text="Question")
    tree.heading("Option 1", text="Option 1")
    tree.heading("Option 2", text="Option 2")
    tree.heading("Option 3", text="Option 3")
    tree.heading("Option 4", text="Option 4")
    tree.heading("Answer", text="Answer")

    # Add data to the Treeview
    for row in data:
        tree.insert("", "end", values=row)

    # Create a horizontal scrollbar
    scrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL, command=tree.xview)
    scrollbar.pack(side=BOTTOM, fill=X)

    # Configure Treeview to use scrollbar
    tree.configure(xscrollcommand=scrollbar.set)


    window.mainloop()

# Get database name and quiz name from command-line arguments
dbName = sys.argv[1]
quizName = sys.argv[2]

# Call the function to display the data
display_data(dbName, quizName)
