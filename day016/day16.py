import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# File for saving data
DATA_FILE = "todo_data.json"

def load_data():
    """Load data from JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("600x700")

        # Load existing data
        self.data = load_data()

        # Main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.main_frame, font=("Arial", 14))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.main_frame, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, pady=10, padx=10)

        # Adding buttons to the frame with evenly distributed space
        self.add_list_button = tk.Button(self.button_frame, text="Add List", command=self.add_list, font=("Arial", 12))
        self.add_list_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.edit_list_button = tk.Button(self.button_frame, text="Edit List", command=self.edit_list, font=("Arial", 12))
        self.edit_list_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.delete_list_button = tk.Button(self.button_frame, text="Delete List", command=self.delete_list, font=("Arial", 12))
        self.delete_list_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.populate_lists()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def populate_lists(self):
        """Populate the main listbox with available lists, adding task count."""
        self.listbox.delete(0, tk.END)
        for idx, list_name in enumerate(self.data, start=1):
            task_count = len(self.data[list_name])  # Get the number of tasks in the list
            self.listbox.insert(tk.END, f"{idx}. {list_name} ({task_count} tasks)")  # Only display the list name and task count

    def add_list(self):
        """Add a new list."""
        list_name = simpledialog.askstring("Add List", "Enter the name of the new list:", parent=self.root)
        if list_name:
            if list_name in self.data:
                messagebox.showerror("Error", "List already exists!")
            else:
                self.data[list_name] = []
                self.populate_lists()

    def edit_list(self):
        """Edit the tasks in the selected list."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a list to edit.")
            return

        list_name_with_tasks = self.listbox.get(selected[0])
        list_name = list_name_with_tasks.split(". ")[1].split(" (")[0]   # Extract list name without task count

        # Check if the list exists in the data before proceeding
        if list_name in self.data:
            TaskManager(self.root, list_name, self.data, self.populate_lists)
        else:
            messagebox.showerror("Error", "List not found!")

    def delete_list(self):
        """Delete the selected list."""
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a list to delete.")
            return

        list_name_with_tasks = self.listbox.get(selected[0])
        list_name = list_name_with_tasks.split(". ")[1].split(" (")[0]   # Extract list name without task count


        # Check if the list exists in the data before proceeding
        if list_name in self.data:
            if messagebox.askyesno("Confirm", f"Are you sure you want to delete the list '{list_name}'?"):
                del self.data[list_name]
                self.populate_lists()
        else:
            messagebox.showerror("Error", "List not found!")

    def on_close(self):
        """Save data and close the app."""
        save_data(self.data)
        self.root.destroy()

class TaskManager:
    def __init__(self, parent, list_name, data, refresh_callback):
        self.list_name = list_name
        self.data = data
        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(parent)
        self.window.title(f"Tasks in {list_name}")
        self.window.geometry("500x600")

        self.task_listbox = tk.Listbox(self.window, font=("Arial", 14))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.window, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Buttons frame
        self.task_button_frame = tk.Frame(self.window)
        self.task_button_frame.pack(side=tk.LEFT, fill=tk.Y, pady=10, padx=10)

        self.add_task_button = tk.Button(self.task_button_frame, text="Add Task", command=self.add_task, font=("Arial", 12))
        self.add_task_button.pack(fill=tk.X, pady=5)

        self.delete_task_button = tk.Button(self.task_button_frame, text="Delete Task", command=self.delete_task, font=("Arial", 12))
        self.delete_task_button.pack(fill=tk.X, pady=5)

        self.populate_tasks()

        # When the window is closed, refresh the list count
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def populate_tasks(self):
        """Populate the task listbox with tasks, adding numbering."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.data[self.list_name], start=1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

    def add_task(self):
        """Add a new task."""
        task = simpledialog.askstring("Add Task", "Enter the new task:", parent=self.window)
        if task:
            self.data[self.list_name].append(task)
            self.populate_tasks()

    def delete_task(self):
        """Delete the selected task."""
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return

        task = self.task_listbox.get(selected[0]).split(". ")[1]  # Extract task without number
        self.data[self.list_name].remove(task)
        self.populate_tasks()

    def on_close(self):
        """Close the task window and refresh the task count in the main list."""
        self.refresh_callback()  # Refresh the list count in the main window
        self.window.destroy()  # Close the task management window

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
