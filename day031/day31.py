import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string

# Function to count words, characters, and sentences
def count_text_stats():
    text = text_area.get("1.0", "end-1c")  # Get the text from the text area
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    
    # Count words
    words = text.split()
    word_count = len(words)
    
    # Count characters (excluding spaces)
    char_count = len([char for char in text if char not in string.whitespace])
    
    # Count sentences (based on period ".")
    sentences = text.split(".")
    sentence_count = len([sentence for sentence in sentences if sentence.strip() != ""])
    
    # Update the result labels
    word_label.config(text=f"Word count: {word_count}")
    char_label.config(text=f"Character count (excluding spaces): {char_count}")
    sentence_label.config(text=f"Sentence count: {sentence_count}")

# Function to clear the text area
def clear_text():
    text_area.delete("1.0", "end")
    word_label.config(text="Word count: 0")
    char_label.config(text="Character count (excluding spaces): 0")
    sentence_label.config(text="Sentence count: 0")

# Create the main window
root = tk.Tk()
root.title("Word Counter Tool")  # Window title
root.geometry("500x400")  # Window size
root.config(bg="#f7f7f7")  # Background color

# Create the widgets
title_label = ttk.Label(root, text="Enter text for analysis:", font=("Helvetica", 14), background="#f7f7f7")
title_label.pack(pady=10)

text_area = tk.Text(root, height=8, width=50, font=("Helvetica", 12))
text_area.pack(pady=10)

# Buttons
count_button = ttk.Button(root, text="Count", command=count_text_stats)
count_button.pack(pady=10)

clear_button = ttk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

# Result labels
word_label = ttk.Label(root, text="Word count: 0", font=("Helvetica", 12), background="#f7f7f7")
word_label.pack(pady=5)

char_label = ttk.Label(root, text="Character count (excluding spaces): 0", font=("Helvetica", 12), background="#f7f7f7")
char_label.pack(pady=5)

sentence_label = ttk.Label(root, text="Sentence count: 0", font=("Helvetica", 12), background="#f7f7f7")
sentence_label.pack(pady=5)

# Run the application
root.mainloop()
