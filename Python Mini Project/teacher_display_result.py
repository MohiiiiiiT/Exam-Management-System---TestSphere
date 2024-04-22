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
    cursor.execute(f"SELECT stud_username,marks,total_questions FROM {quizName}")
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
    tree = ttk.Treeview(frame, columns=("stud_username", "marks", "total_questions"), show="headings")
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Add columns
    tree.heading("stud_username", text="stud_username")
    tree.heading("marks", text="marks")
    tree.heading("total_questions", text="total_questions")


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
# dbName = "mohit_1"
# quizName = "mohit_1_jabardast1_result"
# Call the function to display the data
display_data(dbName, quizName)
