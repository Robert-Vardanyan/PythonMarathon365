import tkinter as tk
from tkinter import messagebox

# Voting options
candidates = ["Alice", "Bob", "Charlie"]

# Initialize votes dictionary
votes = {candidate: 0 for candidate in candidates}

def vote():
    selected = var.get()
    if selected == "":
        messagebox.showwarning("No selection", "Please select a candidate to vote.")
        return
    votes[selected] += 1
    update_results()
    messagebox.showinfo("Thank you", f"Your vote for {selected} has been recorded.")

def update_results():
    result_text = "Current Votes:\n"
    for candidate, count in votes.items():
        result_text += f"{candidate}: {count}\n"
    results_label.config(text=result_text)

def reset_votes():
    global votes
    votes = {candidate: 0 for candidate in candidates}
    update_results()

# Create main window
root = tk.Tk()
root.title("🗳️ Simple Voting System")
root.geometry("300x350")
root.resizable(False, False)

# Instruction label
tk.Label(root, text="Choose your candidate:", font=("Arial", 14)).pack(pady=10)

# Variable for radio buttons
var = tk.StringVar(value="")

# Radio buttons for candidates
for candidate in candidates:
    tk.Radiobutton(root, text=candidate, variable=var, value=candidate, font=("Arial", 12)).pack(anchor="w", padx=40)

# Vote button
tk.Button(root, text="Vote", command=vote, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=15)

# Results label
results_label = tk.Label(root, text="Current Votes:\n" + "\n".join(f"{c}: 0" for c in candidates),
                         font=("Arial", 12), justify="left")
results_label.pack(pady=10)

# Reset votes button
tk.Button(root, text="Reset Votes", command=reset_votes, bg="#f44336", fg="white", font=("Arial", 12), padx=10, pady=5).pack(pady=5)

# Run the GUI event loop
root.mainloop()
