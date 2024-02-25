import json
import random
import tkinter as tk

def load_ports_data():
    with open('ports.json') as file:
        data = json.load(file)
    random.shuffle(data)  # Shuffle the data to randomize questions
    return data

def check_answer(user_answer, port):
    if user_answer == str(port['Port Number']):
        return "Correct!"
    else:
        return f"Incorrect. The correct answer is {port['Port Number']}."

def display_question():
    global current_question, total_questions
    # Check if the quiz has started
    if current_question < total_questions:
        # If there are more questions to ask
        question = ports_data[current_question]
        question_label.config(text=f"What is the port number for {question['Service name']}?")
    else:
        # If the quiz is over
        question_label.config(text=f"Quiz completed! Your score: {score}/{total_questions}")
        # You may also want to hide the answer entry and submit button here
        answer_entry.pack_forget()
        submit_button.pack_forget()
        reset_button.pack(side=tk.TOP)  # Ensure the reset button is still visible


def submit_answer():
    global current_question, score
    if current_question < total_questions:
        user_answer = answer_entry.get()
        result = check_answer(user_answer, ports_data[current_question])
        result_label.config(text=result)
        if result == "Correct!":
            score += 1
        current_question += 1
        display_question()
        answer_entry.delete(0, tk.END)

def set_number_of_questions():
    global total_questions
    total_questions = int(number_of_questions_entry.get())
    reset_quiz()  # Reset and reshuffle the quiz
    start_quiz()  # Then start the quiz


def start_quiz():
    global quiz_frame, setup_frame, current_question, score
    # Reset the current question index and score
    current_question = 0
    score = 0
    # Hide the number of questions components
    setup_frame.pack_forget()
    # Reset the result label
    result_label.config(text="")
    # Show the quiz components
    quiz_frame.pack()
    # Repack the answer entry
    answer_entry.pack()
    # Repack the submit button
    submit_button.pack(side=tk.TOP)
    # Start the quiz
    display_question()



def reset_quiz():
    global current_question, score, total_questions, ports_data
    current_question = 0
    score = 0
    # Reshuffle the data to get a new order of questions
    random.shuffle(ports_data)
    # Show the number of questions components
    setup_frame.pack()
    # Hide the quiz components
    quiz_frame.pack_forget()
    # Clear the result label
    result_label.config(text="")
    # Clear the answer entry
    answer_entry.delete(0, tk.END)


# Load ports data from the JSON file
ports_data = load_ports_data()

# Initialize variables
current_question = 0
score = 0
total_questions = 5  # Default value

# Create GUI
window = tk.Tk()
window.title("Network Ports Quiz")

# Setup frame
setup_frame = tk.Frame(window)
setup_frame.pack()

number_of_questions_label = tk.Label(setup_frame, text="Number of Questions:")
number_of_questions_label.pack(side=tk.TOP)

number_of_questions_entry = tk.Entry(setup_frame)
number_of_questions_entry.pack(side=tk.TOP)

set_number_of_questions_button = tk.Button(setup_frame, text="Set", command=set_number_of_questions)
set_number_of_questions_button.pack(side=tk.TOP)

# Quiz frame
quiz_frame = tk.Frame(window)

question_label = tk.Label(quiz_frame, text="")
question_label.pack(side=tk.TOP)

answer_entry = tk.Entry(quiz_frame)
answer_entry.pack(side=tk.TOP)

submit_button = tk.Button(quiz_frame, text="Submit", command=submit_answer)
submit_button.pack(side=tk.TOP)

result_label = tk.Label(quiz_frame, text="")
result_label.pack(side=tk.TOP)

reset_button = tk.Button(quiz_frame, text="Reset", command=reset_quiz)
reset_button.pack(side=tk.TOP)


# Start with only the setup frame visible
setup_frame.pack()
quiz_frame.pack_forget()

# Run the GUI event loop
window.mainloop()
