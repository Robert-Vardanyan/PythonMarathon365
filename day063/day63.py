import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_username():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + "_-"
        username = ''.join(random.choices(characters, k=length))
        result_label.config(text=username, fg="#4CAF50")
        root.clipboard_clear()
        root.clipboard_append(username)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid positive number.")

# Main window
root = tk.Tk()
root.title("🔀 Random Username Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Username Generator", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

# Input for length
length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack(pady=5)

tk.Label(length_frame, text="Username Length:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, width=5, font=("Arial", 12))
length_entry.insert(0, "8")
length_entry.pack(side=tk.LEFT)

# Generate button
generate_btn = tk.Button(root, text="Generate Username", command=generate_username, bg="#2196F3", fg="white", font=("Arial", 12), padx=10, pady=5)
generate_btn.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Consolas", 14, "bold"), bg="#f0f0f0", fg="#4CAF50")
result_label.pack(pady=10)

# Start
root.mainloop()
