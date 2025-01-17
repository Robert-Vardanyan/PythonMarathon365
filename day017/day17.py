import tkinter as tk
import random

def generate_nickname():
    first_letter = first_letter_entry.get().strip()
    length = length_entry.get().strip()

    if not first_letter or not first_letter.isalpha() or len(first_letter) > 1:
        result_label.config(text="Error: The first letter must be a single character.")
        return

    if not length.isdigit() or int(length) < 2:
        result_label.config(text="Error: Length must be a number >= 2.")
        return

    length = int(length)

    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxyz"

    nickname = first_letter.upper()

    for i in range(length - 1):
        if nickname[-1].lower() in vowels:
            nickname += random.choice(consonants)
        else:
            nickname += random.choice(vowels)

    result_label.config(text=f"Generated Nickname: {nickname}")

# Create main window
root = tk.Tk()
root.title("Nickname Generator")
root.geometry("500x350")
root.resizable(False, False)

# Create central frame
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(main_frame, text="Nickname Generator", font=("Arial", 16))
title_label.pack(pady=10)

# First letter input field
first_letter_frame = tk.Frame(main_frame)
first_letter_frame.pack(pady=5)
first_letter_label = tk.Label(first_letter_frame, text="First Letter:", font=("Arial", 12))
first_letter_label.pack(side=tk.LEFT, padx=5)
first_letter_entry = tk.Entry(first_letter_frame, font=("Arial", 12), width=5)
first_letter_entry.pack(side=tk.LEFT)

# Nickname length input field
length_frame = tk.Frame(main_frame)
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Nickname Length:", font=("Arial", 12))
length_label.pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, font=("Arial", 12), width=5)
length_entry.pack(side=tk.LEFT)

# Generate button
generate_button = tk.Button(main_frame, text="Generate", font=("Arial", 12), command=generate_nickname, bg="lightblue", fg="black")
generate_button.pack(pady=10)

# Result display field
result_label = tk.Label(main_frame, text="", font=("Arial", 12), bg="lightyellow", fg="black", width=40, height=2)
result_label.pack(pady=10)

# Start main loop
root.mainloop()
