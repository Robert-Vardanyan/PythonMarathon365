import tkinter as tk
from tkinter import ttk
from fractions import Fraction

def calculate():
    try:
        frac1 = Fraction(entry1.get())
        frac2 = Fraction(entry2.get())
        operation = operator.get()

        if operation == "+":
            result = frac1 + frac2
        elif operation == "-":
            result = frac1 - frac2
        elif operation == "*":
            result = frac1 * frac2
        elif operation == "/":
            if frac2 == 0:
                raise ZeroDivisionError
            result = frac1 / frac2
        else:
            result = "Invalid operator"

        result_label.config(text=f"= {result}")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by 0")
    except Exception:
        result_label.config(text="Invalid input (use a/b format)")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="= ?")

# GUI setup
root = tk.Tk()
root.title("Fraction Calculator")
root.geometry("400x200")

frame = ttk.Frame(root, padding=10)
frame.pack(expand=True)

ttk.Label(frame, text="Fraction 1 (e.g., 3/4):").grid(row=0, column=0)
entry1 = ttk.Entry(frame)
entry1.grid(row=0, column=1)

ttk.Label(frame, text="Operation:").grid(row=1, column=0)
operator = ttk.Combobox(frame, values=["+", "-", "*", "/"], width=5)
operator.set("+")
operator.grid(row=1, column=1)

ttk.Label(frame, text="Fraction 2 (e.g., 2/5):").grid(row=2, column=0)
entry2 = ttk.Entry(frame)
entry2.grid(row=2, column=1)

ttk.Button(frame, text="Calculate", command=calculate).grid(row=3, column=0, pady=10)
ttk.Button(frame, text="Clear", command=clear).grid(row=3, column=1, pady=10)

result_label = ttk.Label(frame, text="= ?", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
