import json
import random
import tkinter as tk

def load_ports_data():
    with open('ports.json') as file:
        data = json.load(file)
    return data

def check_answer(user_answer, port):
    if user_answer == str(port['Port Number']):
        return "Correct!"
    else:
        return f"Incorrect. The correct answer is {port['Port Number']}."

def display_question():
    global current_question
    if current_question < len(ports_data):
        question_label.config(text=f"What is the port number for {ports_data[current_question]['Service name']}?")
    else:
        question_label.config(text="Quiz completed!")

def submit_answer():
    global current_question, score
    user_answer = answer_entry.get()
    result = check_answer(user_answer, ports_data[current_question])
    result_label.config(text=result)
    if result == "Correct!":
        score += 1
    current_question += 1
    display_question()
    answer_entry.delete(0, tk.END)

def reset_quiz():
    global current_question, score
    current_question = 0
    score = 0
    display_question()
    result_label.config(text="")
    answer_entry.delete(0, tk.END)

# Load ports data from the JSON file
ports_data = load_ports_data()

# Initialize variables
current_question = 0
score = 0

# Create GUI
window = tk.Tk()
window.title("Network Ports Quiz")

question_label = tk.Label(window, text="")
question_label.pack()

answer_entry = tk.Entry(window)
answer_entry.pack()

submit_button = tk.Button(window, text="Submit", command=submit_answer)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

reset_button = tk.Button(window, text="Reset", command=reset_quiz)
reset_button.pack()

# Display first question
display_question()

# Run the GUI event loop
window.mainloop()

import json
import random
def load_ports_data():
    with open('ports.json') as file:
        data = json.load(file)
    return data

def run_quiz(ports_data):
    score = 0
    total_questions = len(ports_data)
    
    # Shuffle the ports_data list
    random.shuffle(ports_data)
    
    for port in ports_data:
        print(f"What is the port number for {port['Service name']}?")
        user_answer = input("Enter your answer: ")
        
        if user_answer == str(port['Port Number']):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {port['Port Number']}.")
        
        print()
    
    print(f"Quiz completed! You scored {score}/{total_questions}.")

# Load ports data from the JSON file
ports_data = load_ports_data()

# Run the quiz
run_quiz(ports_data)