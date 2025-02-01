import tkinter as tk
import random

# List of possible answers to questions
answers = [
    "Yes", "No", "Maybe", "Ask again later", "Definitely not", 
    "Yes, absolutely!", "I wouldn't count on it", "It's unclear", 
    "Certainly", "Most likely"
]

# Function that selects a random answer
def get_answer():
    answer = random.choice(answers)
    answer_label.config(text=answer)

# Create the main window
root = tk.Tk()
root.title("Magic 8-Ball Game")
root.geometry("400x400")
root.config(bg="black")

# Title label
title_label = tk.Label(root, text="Magic 8-Ball", font=("Helvetica", 24), fg="white", bg="black")
title_label.pack(pady=20)

# Button to get an answer
ask_button = tk.Button(root, text="Ask the Magic 8-Ball", font=("Helvetica", 14), fg="white", bg="blue", command=get_answer)
ask_button.pack(pady=20)

# Create the triangle
canvas = tk.Canvas(root, width=300, height=200, bg="black", bd=0, highlightthickness=0)
canvas.pack(pady=20)

# Label to display the answer inside the triangle
answer_label = tk.Label(root, text="", font=("Helvetica", 18), fg="deepskyblue", bg="black")
answer_label.place(relx=0.5, rely=0.7, anchor="center")

# Start the main loop
root.mainloop()
