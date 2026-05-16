from tkinter import *
from tkinter import messagebox
import random
from tkinter import ttk

# ---------------- QUESTION DATABASE ---------------- #

quiz_data = {

    "Python": {

        "Easy": [

            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "answer": "def"
            },

            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "#", "/*", "$"],
                "answer": "#"
            },

            {
                "question": "Which data type stores multiple values?",
                "options": ["int", "float", "list", "char"],
                "answer": "list"
            },

            {
                "question": "Which function displays output?",
                "options": ["display()", "show()", "print()", "output()"],
                "answer": "print()"
            },

            {
                "question": "Python is a _____ language.",
                "options": ["Low-level", "Machine", "High-level", "Assembly"],
                "answer": "High-level"
            }
        ],

        "Medium": [

            {
                "question": "Which data type is immutable?",
                "options": ["List", "Dictionary", "Set", "Tuple"],
                "answer": "Tuple"
            },

            {
                "question": "Which function is used for input?",
                "options": ["scan()", "cin", "input()", "read()"],
                "answer": "input()"
            },

            {
                "question": "Which keyword is used for loop?",
                "options": ["repeat", "for", "loop", "iterate"],
                "answer": "for"
            },

            {
                "question": "What is the correct file extension for Python?",
                "options": [".java", ".py", ".cpp", ".html"],
                "answer": ".py"
            },

            {
                "question": "Which operator is used for exponent?",
                "options": ["^", "*", "**", "%"],
                "answer": "**"
            }
        ],

        "Hard": [

            {
                "question": "Which module is used for random numbers?",
                "options": ["math", "random", "os", "sys"],
                "answer": "random"
            },

            {
                "question": "Which keyword handles exceptions?",
                "options": ["error", "try", "catch", "final"],
                "answer": "try"
            },

            {
                "question": "Which method adds element to list?",
                "options": ["insert()", "append()", "push()", "add()"],
                "answer": "append()"
            },

            {
                "question": "What does OOP stand for?",
                "options": [
                    "Object Oriented Programming",
                    "Only Object Program",
                    "Object Ordered Program",
                    "Optional Object Programming"
                ],
                "answer": "Object Oriented Programming"
            },

            {
                "question": "Which keyword creates a class?",
                "options": ["define", "function", "class", "object"],
                "answer": "class"
            }
        ]
    },

    "Computer Networks": {

        "Easy": [

            {
                "question": "What does LAN stand for?",
                "options": [
                    "Local Area Network",
                    "Large Area Network",
                    "Light Area Network",
                    "Long Area Network"
                ],
                "answer": "Local Area Network"
            },

            {
                "question": "Which device connects networks?",
                "options": ["Mouse", "Router", "Keyboard", "Monitor"],
                "answer": "Router"
            },

            {
                "question": "Which device forwards packets?",
                "options": ["Router", "Printer", "Scanner", "Speaker"],
                "answer": "Router"
            },

            {
                "question": "What does WAN stand for?",
                "options": [
                    "Wide Area Network",
                    "Wireless Area Network",
                    "World Area Network",
                    "Web Area Network"
                ],
                "answer": "Wide Area Network"
            },

            {
                "question": "Which topology uses a single cable?",
                "options": ["Star", "Ring", "Bus", "Mesh"],
                "answer": "Bus"
            }
        ],

        "Medium": [

            {
                "question": "Which protocol is used for web browsing?",
                "options": ["FTP", "HTTP", "SMTP", "TCP"],
                "answer": "HTTP"
            },

            {
                "question": "Which layer handles routing?",
                "options": ["Transport", "Network", "Session", "Physical"],
                "answer": "Network"
            },

            {
                "question": "Which protocol transfers files?",
                "options": ["HTTP", "FTP", "SMTP", "ARP"],
                "answer": "FTP"
            },

            {
                "question": "What does IP stand for?",
                "options": [
                    "Internet Protocol",
                    "Internal Process",
                    "Internet Process",
                    "Input Protocol"
                ],
                "answer": "Internet Protocol"
            },

            {
                "question": "Which layer handles error detection?",
                "options": ["Data Link", "Session", "Application", "Presentation"],
                "answer": "Data Link"
            }
        ],

        "Hard": [

            {
                "question": "Which topology uses central hub?",
                "options": ["Bus", "Ring", "Star", "Mesh"],
                "answer": "Star"
            },

            {
                "question": "Which protocol is connection-oriented?",
                "options": ["UDP", "IP", "TCP", "ARP"],
                "answer": "TCP"
            },

            {
                "question": "Which protocol sends emails?",
                "options": ["SMTP", "HTTP", "FTP", "TCP"],
                "answer": "SMTP"
            },

            {
                "question": "Which device works at Data Link layer?",
                "options": ["Hub", "Switch", "Router", "Repeater"],
                "answer": "Switch"
            },

            {
                "question": "What is the default port number of HTTP?",
                "options": ["21", "25", "80", "110"],
                "answer": "80"
            }
        ]
    },

    "DBMS": {

        "Easy": [

            {
                "question": "What does DBMS stand for?",
                "options": [
                    "Database Management System",
                    "Data Backup Management System",
                    "Digital Base Management System",
                    "Database Monitoring System"
                ],
                "answer": "Database Management System"
            },

            {
                "question": "Which language is used in DBMS?",
                "options": ["HTML", "SQL", "Python", "Java"],
                "answer": "SQL"
            },

            {
                "question": "Which key uniquely identifies a record?",
                "options": ["Foreign Key", "Primary Key", "Candidate Key", "Super Key"],
                "answer": "Primary Key"
            },

            {
                "question": "Rows in database table are called?",
                "options": ["Fields", "Columns", "Records", "Keys"],
                "answer": "Records"
            },

            {
                "question": "Which command retrieves data?",
                "options": ["GET", "SELECT", "OPEN", "SHOW"],
                "answer": "SELECT"
            }
        ],

        "Medium": [

            {
                "question": "Which normal form removes partial dependency?",
                "options": ["1NF", "2NF", "3NF", "BCNF"],
                "answer": "2NF"
            },

            {
                "question": "Which SQL command deletes table?",
                "options": ["REMOVE", "DELETE", "DROP", "CLEAR"],
                "answer": "DROP"
            },

            {
                "question": "Which join returns matching rows?",
                "options": ["INNER JOIN", "OUTER JOIN", "LEFT JOIN", "RIGHT JOIN"],
                "answer": "INNER JOIN"
            },

            {
                "question": "Which command updates data?",
                "options": ["MODIFY", "UPDATE", "CHANGE", "ALTER"],
                "answer": "UPDATE"
            },

            {
                "question": "Which clause filters records?",
                "options": ["WHERE", "ORDER BY", "GROUP BY", "SORT"],
                "answer": "WHERE"
            }
        ],

        "Hard": [

            {
                "question": "Which key links two tables?",
                "options": ["Primary Key", "Candidate Key", "Foreign Key", "Unique Key"],
                "answer": "Foreign Key"
            },

            {
                "question": "What is ACID property?",
                "options": [
                    "Database transaction property",
                    "Programming language",
                    "Network protocol",
                    "Data structure"
                ],
                "answer": "Database transaction property"
            },

            {
                "question": "Which SQL command changes table structure?",
                "options": ["CHANGE", "MODIFY", "ALTER", "UPDATE"],
                "answer": "ALTER"
            },

            {
                "question": "Which normal form removes transitive dependency?",
                "options": ["1NF", "2NF", "3NF", "BCNF"],
                "answer": "3NF"
            },

            {
                "question": "Which database model uses tables?",
                "options": ["Hierarchical", "Network", "Relational", "Object"],
                "answer": "Relational"
            }
        ]
    }
}

# ---------------- MAIN WINDOW ---------------- #

root = Tk()
root.title("Advanced Online Quiz System")
root.geometry("750x550")
root.config(bg="#1e1e1e")

# ---------------- VARIABLES ---------------- #

questions = []
q_no = 0
score = 0
timer = 15

correct_answers = 0
wrong_answers = 0
student_name = ""

selected_option = StringVar()
selected_subject = StringVar()
selected_level = StringVar()

# ---------------- FUNCTIONS ---------------- #

def login():

    global student_name

    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username != "" and password != "":

        student_name = username

        login_frame.pack_forget()
        subject_frame.pack(fill="both", expand=True)

    else:
        messagebox.showerror(
            "Error",
            "Please Enter Username and Password"
        )

def start_quiz():

    global questions, q_no, score
    global correct_answers, wrong_answers

    q_no = 0
    score = 0

    correct_answers = 0
    wrong_answers = 0

    subject = selected_subject.get()
    level = selected_level.get()

    if subject == "" or level == "":

        messagebox.showerror(
            "Error",
            "Please Select Subject and Difficulty"
        )
        return

    questions = quiz_data[subject][level]

    random.shuffle(questions)

    subject_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)

    display_question()
    countdown()

def display_question():

    global timer

    timer = 15

    question_number.config(
        text=f"Question {q_no + 1} of {len(questions)}"
    )

    question_label.config(
        text=questions[q_no]["question"]
    )

    options = questions[q_no]["options"]

    selected_option.set("")

    option1.config(text=options[0], value=options[0])
    option2.config(text=options[1], value=options[1])
    option3.config(text=options[2], value=options[2])
    option4.config(text=options[3], value=options[3])

def next_question():

    global q_no, score
    global correct_answers, wrong_answers

    selected = selected_option.get()

    # No Answer Selected
    if selected == "":

        messagebox.showwarning(
            "Warning",
            "Please Select an Answer"
        )
        return

    # Correct Answer
    if selected == questions[q_no]["answer"]:

        score += 1
        correct_answers += 1

        messagebox.showinfo(
            "Result",
            "Correct Answer!"
        )

    # Wrong Answer
    else:

        score -= 0.25
        wrong_answers += 1

        messagebox.showerror(
            "Result",
            f"Wrong Answer!\n\nCorrect Answer: {questions[q_no]['answer']}"
        )

    q_no += 1

    if q_no < len(questions):

        display_question()

    else:

        show_result()

def show_result():

    quiz_frame.pack_forget()

    result_frame.pack(fill="both", expand=True)

    total_questions = len(questions)

    percentage = (score / total_questions) * 100

    # SAVE RESULT IN FILE
    with open("results.txt", "a") as file:

        file.write(
            f"""
Student Name : {student_name}
Final Score : {score}
Correct Answers : {correct_answers}
Wrong Answers : {wrong_answers}
Percentage : {percentage:.2f}%

-------------------------
"""
        )

    result_text.config(
        text=f"""
Quiz Completed!

Student Name : {student_name}

Final Score : {score}

Correct Answers : {correct_answers}

Wrong Answers : {wrong_answers}

Percentage : {percentage:.2f}%
"""
    )
def restart_quiz():

    result_frame.pack_forget()

    selected_subject.set("")
    selected_level.set("")
    selected_option.set("")

    subject_frame.pack(fill="both", expand=True)

def show_leaderboard():

    leaderboard_window = Toplevel(root)

    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("500x400")
    leaderboard_window.config(bg="white")

    title = Label(
        leaderboard_window,
        text="Leaderboard",
        font=("Arial", 20, "bold"),
        bg="white"
    )

    title.pack(pady=10)

    columns = ("Name", "Score", "Percentage")

    tree = ttk.Treeview(
        leaderboard_window,
        columns=columns,
        show="headings"
    )

    tree.heading("Name", text="Name")
    tree.heading("Score", text="Score")
    tree.heading("Percentage", text="Percentage")

    tree.column("Name", width=150)
    tree.column("Score", width=100)
    tree.column("Percentage", width=100)

    tree.pack(fill=BOTH, expand=True, pady=20)

    try:

        with open("results.txt", "r") as file:

            data = file.read().split("-------------------------")

            for entry in data:

                if entry.strip() != "":

                    lines = entry.strip().split("\n")

                    name = lines[0].split(":")[1].strip()
                    score = lines[1].split(":")[1].strip()
                    percentage = lines[4].split(":")[1].strip()

                    tree.insert(
                        "",
                        END,
                        values=(name, score, percentage)
                    )

    except FileNotFoundError:

        messagebox.showerror(
            "Error",
            "No leaderboard data found!"
        )

def countdown():

    global timer

    timer_label.config(
        text=f"Time Left : {timer} sec"
    )

    if timer > 0:

        timer -= 1
        root.after(1000, countdown)

    else:
        next_question()

# ---------------- LOGIN FRAME ---------------- #

login_frame = Frame(root, bg="#1e1e1e")

title = Label(
    login_frame,
    text="ONLINE QUIZ SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=20)

Label(
    login_frame,
    text="Username",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
).pack()

username_entry = Entry(
    login_frame,
    font=("Arial", 14)
)
username_entry.pack(pady=5)

Label(
    login_frame,
    text="Password",
    font=("Arial", 14),
    bg="lightblue"
).pack()

password_entry = Entry(
    login_frame,
    show="*",
    font=("Arial", 14)
)
password_entry.pack(pady=5)

Button(
    login_frame,
    text="Login",
    font=("Arial", 14, "bold"),
    bg="#00adb5",
    fg="white",
    activebackground="#008891",
    activeforeground="white",
    command=login
).pack(pady=20)

login_frame.pack(fill="both", expand=True)

# ---------------- SUBJECT FRAME ---------------- #

subject_frame = Frame(root, bg="#2d2d2d")

Label(
    subject_frame,
    text="Select Subject",
    font=("Arial", 18, "bold"),
    bg="white"
).pack(pady=20)

Radiobutton(
    subject_frame,
    text="Python",
    variable=selected_subject,
    value="Python",
    font=("Arial", 14),
     bg="#2d2d2d",
    fg="white",
    selectcolor="black"
).pack()

Radiobutton(
    subject_frame,
    text="Computer Networks",
    variable=selected_subject,
    value="Computer Networks",
    font=("Arial", 14),
     bg="#2d2d2d",
    fg="white",
    selectcolor="black"
).pack()

Radiobutton(
    subject_frame,
    text="DBMS",
    variable=selected_subject,
    value="DBMS",
    font=("Arial", 14),
    bg="#2d2d2d",
    fg="white",
    selectcolor="black"
).pack()

Label(
    subject_frame,
    text="Select Difficulty Level",
    font=("Arial", 18, "bold"),
    bg="white"
).pack(pady=20)

Radiobutton(
    subject_frame,
    text="Easy",
    variable=selected_level,
    value="Easy",
    font=("Arial", 14),
    bg="#2d2d2d",
     fg="white",
    selectcolor="black"
).pack()

Radiobutton(
    subject_frame,
    text="Medium",
    variable=selected_level,
    value="Medium",
    font=("Arial", 14),
    bg="#2d2d2d",
     fg="white",
    selectcolor="black"
).pack()

Radiobutton(
    subject_frame,
    text="Hard",
    variable=selected_level,
    value="Hard",
    font=("Arial", 14),
    bg="#2d2d2d",
     fg="white",
    selectcolor="black"
).pack()

Button(
    subject_frame,
    text="Start Quiz",
    font=("Arial", 14),
    command=start_quiz
).pack(pady=30)

# ---------------- QUIZ FRAME ---------------- #

quiz_frame = Frame(root, bg="#2d2d2d")

question_number = Label(
    quiz_frame,
    text="",
    font=("Arial", 14),
    bg="white"
)
question_number.pack(pady=10)

timer_label = Label(
    quiz_frame,
    text="",
    font=("Arial", 14, "bold"),
    fg="red",
    bg="white"
)
timer_label.pack()

question_label = Label(
    quiz_frame,
    text="",
    font=("Arial", 16, "bold"),
    wraplength=650,
    bg="#2d2d2d",
    fg="white"
)
question_label.pack(pady=20)

option1 = Radiobutton(
    quiz_frame,
    text="",
    variable=selected_option,
    value="",
    font=("Arial", 13),
    bg="#2d2d2d",
    fg="white"
)
option1.pack(anchor="w", padx=80)

option2 = Radiobutton(
    quiz_frame,
    text="",
    variable=selected_option,
    value="",
    font=("Arial", 13),
    bg="#2d2d2d",
    fg="white"
)
option2.pack(anchor="w", padx=80)

option3 = Radiobutton(
    quiz_frame,
    text="",
    variable=selected_option,
    value="",
    font=("Arial", 13),
    bg="#2d2d2d",
    fg="white"
)
option3.pack(anchor="w", padx=80)

option4 = Radiobutton(
    quiz_frame,
    text="",
    variable=selected_option,
    value="",
    font=("Arial", 13),
    bg="#2d2d2d",
    fg="white"
)
option4.pack(anchor="w", padx=80)

Button(
    quiz_frame,
    text="Next",
    font=("Arial", 14),
    command=next_question
).pack(pady=20)

# ---------------- RESULT FRAME ---------------- #

result_frame = Frame(root, bg="#1e1e1e")

result_text = Label(
    result_frame,
    text="",
    font=("Arial", 22, "bold"),
    bg="lightgreen"
)
result_text.pack(pady=30)

restart_button = Button(
    result_frame,
    text="Restart Quiz",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    command=restart_quiz
)

restart_button.pack(pady=20)

leaderboard_button = Button(
    result_frame,
    text="Leaderboard",
    font=("Arial", 14, "bold"),
    bg="darkgreen",
    fg="white",
    command=show_leaderboard
)

leaderboard_button.pack(pady=10)

# ---------------- RUN APPLICATION ---------------- #

root.mainloop()