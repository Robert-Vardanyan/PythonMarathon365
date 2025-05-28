import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        # Title label
        tk.Label(root, text="Age Calculator", font=("Arial", 18)).pack(pady=10)

        # Instruction label
        tk.Label(root, text="Enter your birth date (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)

        # Entry for birth date
        self.birth_entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.birth_entry.pack(pady=5)

        # Calculate button
        self.calc_button = tk.Button(root, text="Calculate Age", font=("Arial", 14), command=self.calculate_age)
        self.calc_button.pack(pady=15)

        # Label for displaying result
        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg="green")
        self.result_label.pack(pady=10)

    def calculate_age(self):
        birth_str = self.birth_entry.get().strip()

        try:
            birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
            today = datetime.today().date()
            if birth_date > today:
                messagebox.showerror("Invalid Date", "Birth date cannot be in the future.")
                return

            # Calculate full years
            years = today.year - birth_date.year
            # Adjust if birth date hasn't occurred yet this year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                years -= 1

            self.result_label.config(text=f"You are {years} years old.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter the date in YYYY-MM-DD format.")

def main():
    root = tk.Tk()
    app = AgeCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
