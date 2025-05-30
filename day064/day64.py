import tkinter as tk
from tkinter import messagebox

MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    "'": '.----.', '"': '.-..-.', '/': '-..-.',  '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}

REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse():
    text = input_text.get("1.0", tk.END).strip().upper()
    try:
        morse = ' '.join(MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, morse)
    except KeyError:
        messagebox.showerror("Error", "Unsupported characters found.")

def morse_to_text():
    morse = input_text.get("1.0", tk.END).strip()
    try:
        text = ''.join(REVERSE_DICT[code] for code in morse.split(' ') if code in REVERSE_DICT)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, text)
    except KeyError:
        messagebox.showerror("Error", "Invalid Morse code.")

def clear_fields():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("📡 Morse Code Translator")
root.geometry("600x400")
root.config(bg="#f0f0f0")

tk.Label(root, text="Input:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 0))
input_text = tk.Text(root, height=5, font=("Consolas", 12))
input_text.pack(padx=10, pady=5, fill=tk.X)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Text → Morse", command=text_to_morse, bg="#2196F3", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Morse → Text", command=morse_to_text, bg="#4CAF50", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_fields, bg="#f44336", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Output:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 0))
output_text = tk.Text(root, height=5, font=("Consolas", 12), bg="#fff")
output_text.pack(padx=10, pady=5, fill=tk.X)

root.mainloop()
