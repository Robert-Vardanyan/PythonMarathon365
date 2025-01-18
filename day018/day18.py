import tkinter as tk
from tkinter import font
import random

# List of 33 compliments
compliments = [
    "You look amazing today!",
    "Your smile is contagious!",
    "You have a heart of gold!",
    "You are an inspiration to others!",
    "You have great ideas!",
    "You light up every room you walk into!",
    "You have such a kind soul!",
    "Your positivity is infectious!",
    "You are stronger than you think!",
    "You have a brilliant mind!",
    "You are incredibly creative!",
    "Your laughter is the best sound!",
    "You make people feel special!",
    "You are one of a kind!",
    "You radiate confidence and warmth!",
    "You are a great listener!",
    "Your compassion is unparalleled!",
    "You have an eye for beauty!",
    "You are making a difference in the world!",
    "You bring out the best in people!",
    "You have a great sense of humor!",
    "You are so thoughtful and caring!",
    "Your presence is calming and reassuring!",
    "You are full of amazing talents!",
    "You handle challenges with grace and strength!",
    "You inspire those around you to be better!",
    "You are a joy to be around!",
    "Your ideas are always fresh and exciting!",
    "You are a true friend to many!",
    "You have a natural charm and elegance!",
    "Your kindness knows no bounds!",
    "You are capable of achieving anything you set your mind to!"
]

# Function to generate a random compliment
def generate_compliment():
    compliment = random.choice(compliments)
    compliment_label.config(text=compliment)

# Create the main application window
root = tk.Tk()
root.title("Random Compliment Generator")
root.geometry("500x300")
root.configure(bg="#F0F8FF")

# Font settings
title_font = font.Font(family="Helvetica", size=20, weight="bold")
button_font = font.Font(family="Helvetica", size=14)
label_font = font.Font(family="Helvetica", size=16)

# Title label
title_label = tk.Label(root, text="Random Compliment Generator", bg="#F0F8FF", fg="#4682B4", font=title_font)
title_label.pack(pady=20)

# Label to display compliments
compliment_label = tk.Label(root, text="", bg="#F0F8FF", fg="#6A5ACD", font=label_font, wraplength=400, justify="center")
compliment_label.pack(pady=30)

# Button to generate compliments
generate_button = tk.Button(root, text="Generate Compliment", command=generate_compliment, bg="#4682B4", fg="white", font=button_font, relief="raised", padx=10, pady=5)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
