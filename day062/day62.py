import tkinter as tk
from tkinter import filedialog, messagebox
import markdown

def convert_to_html():
    md_text = input_text.get("1.0", tk.END)
    html_result = markdown.markdown(md_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, html_result)

def save_html():
    html_content = output_text.get("1.0", tk.END)
    if not html_content.strip():
        messagebox.showwarning("Empty", "Nothing to save!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        messagebox.showinfo("Saved", f"HTML saved to {file_path}")

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("📝 Markdown to HTML Converter")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Markdown Input:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="nw", padx=10, pady=(10, 0))
input_text = tk.Text(root, height=15, width=100, font=("Consolas", 11))
input_text.pack(padx=10, pady=5)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=5)

convert_btn = tk.Button(btn_frame, text="Convert to HTML", command=convert_to_html, bg="#4CAF50", fg="white", padx=10, pady=5)
convert_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(btn_frame, text="Save HTML", command=save_html, bg="#2196F3", fg="white", padx=10, pady=5)
save_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_all, bg="#f44336", fg="white", padx=10, pady=5)
clear_btn.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="HTML Output:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="nw", padx=10, pady=(10, 0))
output_text = tk.Text(root, height=15, width=100, font=("Consolas", 11), bg="#fefefe")
output_text.pack(padx=10, pady=5)

root.mainloop()
