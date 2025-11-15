from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def setup_window():

    root = Tk()
    root.title("Math Quiz")
    root.attributes('-fullscreen', True)
    root.config(bg="black")
    return root


root = setup_window()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Loads and set background image
bg_image = Image.open(os.path.join(SCRIPT_DIR, "Bgimg.jpg"))
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo

# Loads the frame background image
def load_frame_bg(frame):
    frame_img = Image.open(os.path.join(SCRIPT_DIR, "framebgimg.png"))
    frame.update_idletasks()
    width = int(frame.winfo_width()) if frame.winfo_width() > 1 else 800
    height = int(frame.winfo_height()) if frame.winfo_height() > 1 else 600
    frame_img = frame_img.resize((width, height))
    frame_photo = ImageTk.PhotoImage(frame_img)
    frame_bg_label = Label(frame, image=frame_photo, bd=0, highlightthickness=0)
    frame_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame_bg_label.image = frame_photo 
    frame_bg_label.lower()  
    return frame_bg_label


difficulty_level = None
current_question = 0
total_questions = 10
score = 0
attempts = 0
current_num1 = 0
current_num2 = 0
current_operation = ''
correct_answer = 0


def style_button(button, text, width=200, height=50):
    btn_img = Image.open(os.path.join(SCRIPT_DIR, "buttonsbg.png"))
    btn_img = btn_img.resize((width, height))
    btn_photo = ImageTk.PhotoImage(btn_img)
    
    button.config(
        text=text,
        font=("Arial", 14, "bold"),
        fg="white",
        image=btn_photo,
        compound="center",
        bd=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2"
    )
    button.image = btn_photo

# Random numbers will be generated based on the selected difficulty level and for each question it will randomly choose between -+
def randomInt(difficulty):

    if difficulty == "Easy":
        return random.randint(0, 9)
    elif difficulty == "Moderate":
        return random.randint(10, 99)
    elif difficulty == "Advanced":
        return random.randint(100, 999)
    return 0


def decideOperation():
    return random.choice(['+', '-'])


def displayProblem():
    global current_num1, current_num2, current_operation, correct_answer, attempts
    
    current_num1 = randomInt(difficulty_level)
    current_num2 = randomInt(difficulty_level)
    current_operation = decideOperation()
    
    if current_operation == '+':
        correct_answer = current_num1 + current_num2
    else:
        correct_answer = current_num1 - current_num2
    
    attempts = 0
    
    # Update UI
    question_label.config(text=f"Question {current_question + 1} of {total_questions}")
    problem_label.config(text=f"{current_num1} {current_operation} {current_num2} =")
    answer_entry.delete(0, END)
    feedback_label.config(text="")
    score_label.config(text=f"Score: {score}/100")
    answer_entry.focus()


def isCorrect():
    global score, attempts, current_question
    
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="Please enter a valid number!", fg="red")
        return
    
    attempts += 1
    
    if user_answer == correct_answer:
        if attempts == 1:
            score += 10
            feedback_label.config(text="Correct! +10 points", fg="green")
        else:
            score += 5
            feedback_label.config(text="Correct! +5 points", fg="green")
        
        score_label.config(text=f"Score: {score}/100")
        current_question += 1
        
        if current_question < total_questions:
            root.after(1000, displayProblem)
        else:
            root.after(1000, displayResults)
    else:
        if attempts == 1:
            feedback_label.config(text="Wrong! Try again (one more chance)", fg="orange")
        else:
            feedback_label.config(text=f"Wrong! The correct answer was {correct_answer}", fg="red")
            current_question += 1
            
            if current_question < total_questions:
                root.after(2000, displayProblem)
            else:
                root.after(2000, displayResults)

# Display the finals reults screem and shows the grde which he user has earned based on his score
def displayResults():
    if score >= 95:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B+"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    result_message = f"Quiz Complete!\n\nYour Score: {score}/100\nGrade: {grade}"
    play_again = messagebox.askyesno("Quiz Results", f"{result_message}\n\nWould you like to play again?")
    
    if play_again:
        show_quiz()
    else:
        show_menu()


def start_game(level):
    global difficulty_level, current_question, score
    
    difficulty_level = level
    current_question = 0
    score = 0
    
    quiz_frame.place_forget()
    game_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
    game_frame.lift()
    
    displayProblem()


def show_quiz():
    button_frame.place_forget()
    instructions_frame.place_forget()
    game_frame.place_forget()
    quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
    quiz_frame.lift()


def show_instructions():
    button_frame.place_forget()
    quiz_frame.place_forget()
    game_frame.place_forget()
    instructions_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
    instructions_frame.lift()


def show_menu():
    global current_question, score, attempts
    
    # Reset quiz state when going back to menu
    current_question = 0
    score = 0
    attempts = 0
    
    quiz_frame.place_forget()
    instructions_frame.place_forget()
    game_frame.place_forget()
    button_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
    button_frame.lift()


button_frame = Frame(root, highlightthickness=3, highlightbackground="#3a3a3a")
button_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
button_frame.pack_propagate(False)
load_frame_bg(button_frame)


quiz_frame = Frame(root, highlightthickness=3, highlightbackground="#3a3a3a")
quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
quiz_frame.pack_propagate(False)
load_frame_bg(quiz_frame)


instructions_frame = Frame(root, highlightthickness=3, highlightbackground="#3a3a3a")
instructions_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
instructions_frame.pack_propagate(False)
load_frame_bg(instructions_frame)


game_frame = Frame(root, highlightthickness=3, highlightbackground="#3a3a3a")
game_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.38, relheight=0.48)
game_frame.pack_propagate(False)
load_frame_bg(game_frame)


# Main Menu
menu_title = Label(button_frame, text="Test Your Math Skills!", 
                   font=("Arial", 16), fg="white", bg="grey")
menu_title.pack(pady=(60, 20))

play_button = Button(button_frame, bd=0)
style_button(play_button, "Play")
play_button.pack(pady=12)

instructions_button = Button(button_frame, bd=0)
style_button(instructions_button, "Instructions")
instructions_button.pack(pady=12)

exit_button = Button(button_frame, command=root.destroy, bd=0)
style_button(exit_button, "Exit")
exit_button.pack(pady=12)


# Select Difficulty Screen
difficulty_title = Label(quiz_frame, text="Select Difficulty", 
                        font=("Arial", 28, "bold"), fg="#ffffff", bg="#1C1C1C")
difficulty_title.pack(pady=(20, 10))

# Difficulty Buttons
easy_button = Button(quiz_frame, bd=0)
style_button(easy_button, "Easy")
easy_button.pack(pady=12)

moderate_button = Button(quiz_frame, bd=0)
style_button(moderate_button, "Moderate")
moderate_button.pack(pady=12)

advanced_button = Button(quiz_frame, bd=0)
style_button(advanced_button, "Advanced")
advanced_button.pack(pady=12)

difficulty_back_button = Button(quiz_frame, command=show_menu, bd=0)
style_button(difficulty_back_button, "Back")
difficulty_back_button.pack(pady=(24, 8))

# Quiz Game Screen
question_label = Label(game_frame, text="Question 1 of 10", font=("Arial", 16), 
                      fg="#cccccc", bg="#1C1C1C")
question_label.pack(pady=(20, 5))

problem_label = Label(game_frame, text="", font=("Arial", 42, "bold"), 
                     fg="#ffffff", bg="#1C1C1C")
problem_label.pack(pady=15)

answer_frame = Frame(game_frame, bg="#1C1C1C")
answer_frame.pack(pady=15)

answer_label = Label(answer_frame, text="Your Answer:", font=("Arial", 14),
                    fg="#ffffff", bg="#1C1C1C")
answer_label.pack(pady=(0, 8))

answer_entry = Entry(answer_frame, font=("Arial", 28), width=12, justify=CENTER,
                    bd=2, relief="solid")
answer_entry.pack(padx=10)
answer_entry.bind('<Return>', lambda e: isCorrect())

# Loads the button background for submit button
submit_btn_img = Image.open(os.path.join(SCRIPT_DIR, "buttonsbg.png"))
submit_btn_img = submit_btn_img.resize((220, 50))
submit_btn_photo = ImageTk.PhotoImage(submit_btn_img)

submit_button = Button(answer_frame, text="Submit Answer", command=isCorrect, 
                      font=("Arial", 14, "bold"), fg="white",
                      image=submit_btn_photo, compound="center",
                      cursor="hand2", bd=0, relief="flat", highlightthickness=0)
submit_button.image = submit_btn_photo
submit_button.pack(pady=(15, 0))

feedback_label = Label(game_frame, text="", font=("Arial", 18, "bold"), 
                      fg="white", bg="#1C1C1C")
feedback_label.pack(pady=15)

score_label = Label(game_frame, text="Score: 0/100", font=("Arial", 16, "bold"), 
                   fg="#4CAF50", bg="#1C1C1C")
score_label.pack(pady=8)

# Loads the button background for back button
back_btn_img = Image.open(os.path.join(SCRIPT_DIR, "buttonsbg.png"))
back_btn_img = back_btn_img.resize((180, 40))
back_btn_photo = ImageTk.PhotoImage(back_btn_img)

game_back_button = Button(game_frame, text="< Back to Menu", command=show_menu,
                         font=("Arial", 11), fg="white",
                         image=back_btn_photo, compound="center",
                         cursor="hand2", bd=0, relief="flat", highlightthickness=0)
game_back_button.image = back_btn_photo
game_back_button.pack(pady=10)


# Instructions Screen
instructions_title = Label(instructions_frame, text="How to Play", 
                          font=("Arial", 32, "bold"), fg="#F0F5F0", bg="#1C1C1C")
instructions_title.pack(pady=(40, 30))

instructions_text = Label(instructions_frame, 
                         text="1. You can select between 3 different difficulty levels Easy,Moderate, and Advanced levels and each difficulty is out of 100 points\n\n"
                              "2. Each difficulty contains 10 different questions\n\n"
                              "3. Each question will be either addition or subtraction\n\n"
                              "4. Attempt 1 = 10 points, attempt 2 = 5 points\n\n"
                              "5. Easy: Single digit numbers (0-9)\n\n"
                              "6. Moderate: Double digit numbers (10-99)\n\n"
                              "7. Advanced: 4-digit numbers (100-999)\n\n"
                              "                                    Good luck and have fun!     ",
                              
                         font=("Arial", 10), fg="#ffffff", bg="#1C1C1C",
                         justify=LEFT, wraplength=450)
instructions_text.pack(pady=10, padx=30)

instructions_back = Button(instructions_frame, command=show_menu, bd=0)
style_button(instructions_back, "Back")
instructions_back.pack(pady=30)


# allows us to connect buttons to their functions
play_button.config(command=show_quiz)
instructions_button.config(command=show_instructions)

easy_button.config(command=lambda: start_game("Easy"))
moderate_button.config(command=lambda: start_game("Moderate"))
advanced_button.config(command=lambda: start_game("Advanced"))

show_menu()
root.mainloop()
