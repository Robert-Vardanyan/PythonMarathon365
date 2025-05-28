import tkinter as tk
from tkinter import messagebox

class AcronymGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Acronym Generator")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        # Title label
        tk.Label(root, text="Acronym Generator", font=("Arial", 18)).pack(pady=15)

        # Instruction label
        tk.Label(root, text="Enter a phrase:", font=("Arial", 12)).pack()

        # Entry for phrase input
        self.phrase_entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.phrase_entry.pack(pady=10)

        # Button to generate acronym
        self.generate_button = tk.Button(root, text="Generate Acronym", font=("Arial", 14), command=self.generate_acronym)
        self.generate_button.pack(pady=15)

        # Label to display result
        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.result_label.pack(pady=10)

    def generate_acronym(self):
        phrase = self.phrase_entry.get().strip()
        if not phrase:
            messagebox.showwarning("Input Error", "Please enter a phrase.")
            return

        # Split phrase into words, take first letter of each, make uppercase
        words = phrase.split()
        acronym = "".join(word[0].upper() for word in words if word)

        self.result_label.config(text=f"Acronym: {acronym}")

def main():
    root = tk.Tk()
    app = AcronymGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
