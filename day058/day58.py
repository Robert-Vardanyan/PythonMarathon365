import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    if not name or not phone:
        messagebox.showwarning("Input error", "Please enter both name and phone number.")
        return
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
    else:
        contacts[name] = phone
        listbox_contacts.insert(tk.END, f"{name}: {phone}")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

def remove_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Selection error", "Please select a contact to remove.")
        return
    idx = selected[0]
    contact_str = listbox_contacts.get(idx)
    name = contact_str.split(":")[0]
    del contacts[name]
    listbox_contacts.delete(idx)

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for name, phone in contacts.items():
        listbox_contacts.insert(tk.END, f"{name}: {phone}")

# Создаем окно
root = tk.Tk()
root.title("Simple Contact Book")

# Метки и поля ввода
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

# Кнопки
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=0, column=2, padx=5, pady=5)

btn_remove = tk.Button(root, text="Remove Contact", command=remove_contact)
btn_remove.grid(row=1, column=2, padx=5, pady=5)

btn_view = tk.Button(root, text="View Contacts", command=view_contacts)
btn_view.grid(row=2, column=2, padx=5, pady=5)

# Список контактов
listbox_contacts = tk.Listbox(root, width=40)
listbox_contacts.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
