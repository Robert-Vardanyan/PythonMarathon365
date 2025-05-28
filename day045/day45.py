import tkinter as tk
from tkinter import messagebox

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Grocery Shopping List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill=tk.X)

        self.add_button = tk.Button(root, text="➕ Add Item", font=("Arial", 12), command=self.add_item)
        self.add_button.pack(pady=5)

        frame = tk.Frame(root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame, font=("Arial", 14), yscrollcommand=self.scrollbar.set, height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.listbox.yview)

        self.delete_button = tk.Button(root, text="🗑 Remove Selected", command=self.remove_item)
        self.delete_button.pack(pady=5)

    def add_item(self):
        item = self.entry.get().strip()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item.")

    def remove_item(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])
        else:
            messagebox.showinfo("No Selection", "Please select an item to remove.")

def main():
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
