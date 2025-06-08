import tkinter as tk
from tkinter import ttk
from collections import Counter
import re

def count_words():
    text = input_text.get("1.0", tk.END)
    words = re.findall(r'\b\w+\b', text.lower())
    freq = Counter(words)

    result_text.delete("1.0", tk.END)
    for word, count in freq.most_common():
        result_text.insert(tk.END, f"{word}: {count}\n")

def clear():
    input_text.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Word Frequency Counter")
root.geometry("700x500")

# Input area
ttk.Label(root, text="Enter text:").pack(pady=5)
input_text = tk.Text(root, height=10, wrap=tk.WORD)
input_text.pack(fill=tk.BOTH, expand=True, padx=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Count Words", command=count_words).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Clear", command=clear).grid(row=0, column=1, padx=10)

# Result area
ttk.Label(root, text="Word Frequencies:").pack(pady=5)
result_text = tk.Text(root, height=10, wrap=tk.WORD)
result_text.pack(fill=tk.BOTH, expand=True, padx=10)

root.mainloop()
