import tkinter as tk
from tkinter import messagebox

# Caesar Cipher function
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == "decrypt":
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

# Encrypt button function
def encrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        encrypted = caesar_cipher(text, shift, "encrypt")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift number.")

# Decrypt button function
def decrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        decrypted = caesar_cipher(text, shift, "decrypt")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift number.")

# Clear input and output
def clear_fields():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)

# UI setup
root = tk.Tk()
root.title("🔐 Caesar Cipher Encoder/Decoder")
root.geometry("600x450")
root.config(bg="#f0f0f0")

# Input
tk.Label(root, text="Input Text:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 0))
input_text = tk.Text(root, height=5, font=("Consolas", 12))
input_text.pack(padx=10, pady=5, fill=tk.X)

# Shift input
shift_frame = tk.Frame(root, bg="#f0f0f0")
shift_frame.pack(pady=5)
tk.Label(shift_frame, text="Shift:", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT)
shift_entry = tk.Entry(shift_frame, width=5, font=("Consolas", 12))
shift_entry.pack(side=tk.LEFT, padx=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Encrypt", command=encrypt_text, bg="#4CAF50", fg="white", padx=12, pady=5).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Decrypt", command=decrypt_text, bg="#2196F3", fg="white", padx=12, pady=5).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_fields, bg="#f44336", fg="white", padx=12, pady=5).pack(side=tk.LEFT, padx=5)

# Output
tk.Label(root, text="Output Text:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=(10, 0))
output_text = tk.Text(root, height=5, font=("Consolas", 12), bg="#fff")
output_text.pack(padx=10, pady=5, fill=tk.X)

# Run the application
root.mainloop()
