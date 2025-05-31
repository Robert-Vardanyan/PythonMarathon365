import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker
import language_tool_python


spell = SpellChecker(language='en')  
tool = language_tool_python.LanguageTool('en-US')  

def check_word():
    word = entry.get().strip()
    if not word:
        messagebox.showinfo("Result", "Please enter a word.")
        return
    if word.lower() in spell:
        messagebox.showinfo("Result", f"'{word}' is spelled correctly.")
    else:
        suggestions = spell.candidates(word)
        messagebox.showinfo("Suggestions", f"Suggestions for '{word}':\n" + ", ".join(suggestions))

def check_text():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("Result", "Please enter some text.")
        return
    matches = tool.check(text)
    if not matches:
        messagebox.showinfo("Result", "No issues found.")
    else:
        result = ""
        for match in matches:
            result += f"{match.message}\n→ Suggestion: {', '.join(match.replacements)}\n\n"
        messagebox.showinfo("LanguageTool Results", result)

# UI
root = tk.Tk()
root.title("Spelling & Grammar Checker")
root.geometry("500x400")


tk.Label(root, text="Check a word (SpellChecker):").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
tk.Button(root, text="Check Word", command=check_word).pack(pady=5)


tk.Label(root, text="Check full text (LanguageTool):").pack(pady=10)
text_box = tk.Text(root, height=8, font=("Arial", 12))
text_box.pack(padx=10, pady=5)
tk.Button(root, text="Check Text", command=check_text).pack(pady=5)

root.mainloop()
