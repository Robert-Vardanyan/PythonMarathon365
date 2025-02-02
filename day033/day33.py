import tkinter as tk
import random

class RandomNamePicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Name Picker")
        self.root.geometry("400x600")
        self.root.config(bg="#f4f4f9")
        
        self.names = []

        # Title
        self.title_label = tk.Label(self.root, text="Random Name Picker", font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="#333")
        self.title_label.pack(pady=20)

        # Added names list
        self.names_list_label = tk.Label(self.root, text="Added Names:", font=("Helvetica", 12), bg="#f4f4f9")
        self.names_list_label.pack()

        # Scrollable frame
        self.scroll_frame = tk.Frame(self.root)
        self.scroll_frame.pack(pady=10)

        # Canvas for scrolling
        self.canvas = tk.Canvas(self.scroll_frame, height=150, width=350)
        self.canvas.pack(side="left")

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Frame inside canvas for the list
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Name input
        self.name_entry_label = tk.Label(self.root, text="Enter a name:", font=("Helvetica", 12), bg="#f4f4f9")
        self.name_entry_label.pack()

        self.name_entry = tk.Entry(self.root, font=("Helvetica", 14), width=25)
        self.name_entry.pack(pady=10)

        # Add button
        self.add_button = tk.Button(self.root, text="Add Name", font=("Helvetica", 12), command=self.add_name, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=5)

        # Pick random name button
        self.pick_button = tk.Button(self.root, text="Pick a Random Name", font=("Helvetica", 12), command=self.pick_name, bg="#2196F3", fg="white")
        self.pick_button.pack(pady=5)

        # Label for selected name
        self.result_label = tk.Label(self.root, text="Selected Name will appear here", font=("Helvetica", 14, "italic"), bg="#f4f4f9", fg="#333")
        self.result_label.pack(pady=20)

        # Clear all names button
        self.clear_button = tk.Button(self.root, text="Clear All Names", font=("Helvetica", 12), command=self.clear_names, bg="#F44336", fg="white")
        self.clear_button.pack(pady=5)

    def add_name(self):
        name = self.name_entry.get()
        if name:
            self.names.append(name)
            self.update_names_list()
            self.name_entry.delete(0, tk.END)
            self.result_label.config(text=f"Name '{name}' added!")
        else:
            self.result_label.config(text="Please enter a name to add.")

    def pick_name(self):
        if self.names:
            selected_name = random.choice(self.names)
            self.result_label.config(text=f"Selected: {selected_name}")
        else:
            self.result_label.config(text="No names to pick! Add some first.")

    def clear_names(self):
        self.names.clear()
        self.update_names_list()
        self.result_label.config(text="All names cleared.")

    def update_names_list(self):
        # Clear list
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Add names to the list
        for name in self.names:
            label = tk.Label(self.frame, text=name, font=("Helvetica", 12), bg="#f4f4f9")
            label.pack(anchor="w", pady=2)

        # Update canvas size
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.scrollbar.config(command=self.canvas.yview)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNamePicker(root)
    root.mainloop()
