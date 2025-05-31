import tkinter as tk
from tkinter import messagebox

# Function to generate the story
def generate_story():
    # Get input from entries
    noun1 = entry_noun1.get()
    noun2 = entry_noun2.get()
    adjective1 = entry_adj1.get()
    adjective2 = entry_adj2.get()
    verb1 = entry_verb1.get()
    verb2 = entry_verb2.get()

    # Check that all fields are filled
    if not all([noun1, noun2, adjective1, adjective2, verb1, verb2]):
        messagebox.showwarning("Missing Input", "Please fill in all fields!")
        return

    # Mad Libs story template
    story = (f"Today I went to the {noun1}. "
             f"It was very {adjective1} and {adjective2}. "
             f"I decided to {verb1} with a {noun2}. "
             f"Then, we both {verb2} happily ever after!")

    # Display story in text box
    text_story.config(state="normal")
    text_story.delete("1.0", tk.END)
    text_story.insert(tk.END, story)
    text_story.config(state="disabled")

# Setup window
root = tk.Tk()
root.title("Mad Libs Generator")
root.geometry("450x400")

# Labels and entries for inputs
tk.Label(root, text="Noun 1:").pack()
entry_noun1 = tk.Entry(root)
entry_noun1.pack()

tk.Label(root, text="Noun 2:").pack()
entry_noun2 = tk.Entry(root)
entry_noun2.pack()

tk.Label(root, text="Adjective 1:").pack()
entry_adj1 = tk.Entry(root)
entry_adj1.pack()

tk.Label(root, text="Adjective 2:").pack()
entry_adj2 = tk.Entry(root)
entry_adj2.pack()

tk.Label(root, text="Verb 1:").pack()
entry_verb1 = tk.Entry(root)
entry_verb1.pack()

tk.Label(root, text="Verb 2:").pack()
entry_verb2 = tk.Entry(root)
entry_verb2.pack()

# Button to generate story
btn_generate = tk.Button(root, text="Generate Story", command=generate_story)
btn_generate.pack(pady=10)

# Text box to display story
text_story = tk.Text(root, height=6, width=50, state="disabled", wrap="word")
text_story.pack(pady=10)

root.mainloop()
