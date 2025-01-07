import tkinter as tk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_off():
    root.quit()

def button_sqrt():
    current = entry.get()
    try:
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_percent():
    current = entry.get()
    try:
        result = float(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_equal():
    current = entry.get()
    try:
        result = eval(current.replace('x', '*').replace('/', '/').replace('%', '/100').replace('√', 'math.sqrt'))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating the window
root = tk.Tk()
root.title("Calculator")
root.config(bg="black")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 24), bg="black", fg="white", bd=10, insertbackground="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Buttons
buttons = [
    ('C', 1, 0), ('Off', 1, 1), ('√', 1, 2), ('%', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('x', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

# Placing buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=button_equal).grid(row=row, column=col, padx=10, pady=10)
    elif text == "C":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=button_clear).grid(row=row, column=col, padx=10, pady=10)
    elif text == "Off":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="orange", fg="white", command=button_off).grid(row=row, column=col, padx=10, pady=10)
    elif text == "√":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=button_sqrt).grid(row=row, column=col, padx=10, pady=10)
    elif text == "%":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=button_percent).grid(row=row, column=col, padx=10, pady=10)
    elif text == "+":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=lambda value=text: button_click(value)).grid(row=row, column=col, padx=10, pady=10)
    elif text == ".":
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=lambda value=text: button_click(value)).grid(row=row, column=col, padx=10, pady=10)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), bg="gray", fg="white", command=lambda value=text: button_click(value)).grid(row=row, column=col, padx=10, pady=10)

# Running the window
root.mainloop()
