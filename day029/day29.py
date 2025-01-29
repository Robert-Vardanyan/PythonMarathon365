import random
import tkinter as tk
from tkinter import messagebox

def roll_dice():
    """Roll a dice with the selected number of sides."""
    try:
        sides = int(sides_entry.get())
        if sides < 2:
            messagebox.showerror("Error", "A dice must have at least 2 sides.")
            return
        result = random.randint(1, sides)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Virtual Dice Roller")
root.geometry("300x200")

# Create widgets
tk.Label(root, text="Enter the number of sides on the dice:").pack(pady=5)
sides_entry = tk.Entry(root, width=15)
sides_entry.pack(pady=5)
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=5)

# Run the application
root.mainloop()
