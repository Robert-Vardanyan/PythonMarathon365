import tkinter as tk
from tkinter import messagebox
import hashlib
import json
import os
import pyperclip

# File to store shortened URLs
DATA_FILE = 'urls.json'

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        url_data = json.load(f)
else:
    url_data = {}

# Save data
def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(url_data, f)

# Generate short hash for the URL
def shorten_url():
    url = entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL!")
        return
    short = hashlib.md5(url.encode()).hexdigest()[:6]
    url_data[short] = url
    save_data()
    shortened.set(f"http://short.ly/{short}")

def copy_to_clipboard():
    pyperclip.copy(shortened.get())
    messagebox.showinfo("Copied", "Short URL copied to clipboard!")

def expand_url():
    short_code = entry.get().replace("http://short.ly/", "")
    if short_code in url_data:
        shortened.set(f"Original URL: {url_data[short_code]}")
    else:
        shortened.set("No such short URL found.")

# GUI setup
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="Enter URL or Short Code:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Shorten", width=10, command=shorten_url).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Expand", width=10, command=expand_url).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Copy", width=10, command=copy_to_clipboard).grid(row=0, column=2, padx=5)

shortened = tk.StringVar()
tk.Label(root, textvariable=shortened, font=("Arial", 12), fg="blue").pack(pady=10)

root.mainloop()
