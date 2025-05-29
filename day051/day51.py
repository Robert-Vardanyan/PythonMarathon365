import tkinter as tk
from tkinter import messagebox

class PollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Poll Creator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.question_label = tk.Label(root, text="Enter Poll Question:", font=("Arial", 12))
        self.question_label.pack(pady=5)

        self.question_entry = tk.Entry(root, font=("Arial", 14), width=35)
        self.question_entry.pack(pady=5)

        self.options_label = tk.Label(root, text="Enter up to 4 Options (one per line):", font=("Arial", 12))
        self.options_label.pack(pady=5)

        self.options_text = tk.Text(root, font=("Arial", 12), height=5, width=35)
        self.options_text.pack(pady=5)

        self.create_button = tk.Button(root, text="Create Poll", font=("Arial", 14), command=self.create_poll)
        self.create_button.pack(pady=10)

        self.vote_frame = None
        self.results_label = None

    def create_poll(self):
        question = self.question_entry.get().strip()
        options = self.options_text.get("1.0", tk.END).strip().split("\n")
        options = [opt for opt in options if opt.strip()]

        if not question or len(options) < 2:
            messagebox.showwarning("Input Error", "Please enter a question and at least 2 options.")
            return

        if len(options) > 4:
            messagebox.showwarning("Limit Exceeded", "You can enter up to 4 options.")
            return

        if self.vote_frame:
            self.vote_frame.destroy()

        self.votes = [0] * len(options)
        self.vote_frame = tk.Frame(self.root)
        self.vote_frame.pack(pady=10)

        tk.Label(self.vote_frame, text=question, font=("Arial", 14, "bold")).pack(pady=5)

        self.selected_option = tk.IntVar(value=-1)

        for i, option in enumerate(options):
            tk.Radiobutton(
                self.vote_frame, text=option, variable=self.selected_option, value=i, font=("Arial", 12)
            ).pack(anchor='w')

        tk.Button(
            self.vote_frame, text="Vote", font=("Arial", 12), command=self.submit_vote
        ).pack(pady=10)

        self.results_label = tk.Label(self.vote_frame, text="", font=("Arial", 12), fg="green")
        self.results_label.pack()

        self.poll_options = options

    def submit_vote(self):
        index = self.selected_option.get()
        if index == -1:
            messagebox.showinfo("No Selection", "Please select an option before voting.")
            return

        self.votes[index] += 1
        self.update_results()

    def update_results(self):
        result_text = "Results:\n"
        total = sum(self.votes)
        for opt, vote in zip(self.poll_options, self.votes):
            percent = (vote / total * 100) if total > 0 else 0
            result_text += f"{opt}: {vote} vote(s) - {percent:.1f}%\n"

        self.results_label.config(text=result_text)

def main():
    root = tk.Tk()
    app = PollApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
