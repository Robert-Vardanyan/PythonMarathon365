import tkinter as tk
from tkinter import messagebox

class GradeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Calculator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        tk.Label(root, text="Grade Calculator", font=("Arial", 18)).pack(pady=10)

        tk.Label(root, text="Enter your grades and their weights.\nLeave empty to skip a row.", font=("Arial", 10)).pack()

        self.entries = []
        for i in range(5):  
            frame = tk.Frame(root)
            frame.pack(pady=5)

            grade_label = tk.Label(frame, text=f"Grade {i+1}:")
            grade_label.pack(side=tk.LEFT, padx=5)
            grade_entry = tk.Entry(frame, width=5)
            grade_entry.pack(side=tk.LEFT)

            weight_label = tk.Label(frame, text="Weight:")
            weight_label.pack(side=tk.LEFT, padx=5)
            weight_entry = tk.Entry(frame, width=5)
            weight_entry.pack(side=tk.LEFT)

            self.entries.append((grade_entry, weight_entry))

        self.calc_button = tk.Button(root, text="Calculate Average", font=("Arial", 14), command=self.calculate)
        self.calc_button.pack(pady=15)

        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg="green")
        self.result_label.pack(pady=10)

    def calculate(self):
        total_weight = 0
        weighted_sum = 0

        for grade_entry, weight_entry in self.entries:
            grade_text = grade_entry.get().strip()
            weight_text = weight_entry.get().strip()

            if grade_text == "" and weight_text == "":
                continue

            try:
                grade = float(grade_text)
                weight = float(weight_text)
                if grade < 0 or grade > 100 or weight <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Input error", "Please enter valid grades (0-100) and positive weights.")
                return

            weighted_sum += grade * weight
            total_weight += weight

        if total_weight == 0:
            messagebox.showwarning("No data", "Please enter at least one grade with weight.")
            return

        average = weighted_sum / total_weight
        self.result_label.config(text=f"Weighted Average: {average:.2f}%")

def main():
    root = tk.Tk()
    app = GradeCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
