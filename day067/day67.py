import tkinter as tk
from tkinter import messagebox
import random

def generate_numbers():
    try:
        count = int(entry_count.get())
        max_num = int(entry_max.get())
        if count > max_num:
            messagebox.showerror("Error", "Count can't be greater than max number.")
            return
        
        numbers = random.sample(range(1, max_num + 1), count)
        numbers.sort()
        result_var.set("Your lottery numbers: " + ", ".join(map(str, numbers)))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

def clear_result():
    result_var.set("")
    entry_count.delete(0, tk.END)
    entry_max.delete(0, tk.END)

# Setup window
root = tk.Tk()
root.title("🎲 Lottery Number Generator")
root.geometry("600x300")
root.config(bg="#f0f0f0")

# Instructions
tk.Label(root, text="How many numbers to draw?", bg="#f0f0f0", font=("Arial", 12)).pack(pady=(10,0))
entry_count = tk.Entry(root, font=("Arial", 14), justify="center")
entry_count.pack(pady=5)

tk.Label(root, text="Max number in range?", bg="#f0f0f0", font=("Arial", 12)).pack(pady=(10,0))
entry_max = tk.Entry(root, font=("Arial", 14), justify="center")
entry_max.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate", command=generate_numbers, bg="#4CAF50", fg="white", padx=12, pady=6).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_result, bg="#f44336", fg="white", padx=12, pady=6).pack(side=tk.LEFT, padx=10)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, bg="#f0f0f0", font=("Arial", 14), fg="#333")
result_label.pack(pady=10)

root.mainloop()
