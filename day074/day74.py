import tkinter as tk
import random

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def hex_to_rgb(hex_color):
    # Convert hex color string (#RRGGBB) to a tuple (R, G, B)
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def pick_color():
    color = random_color()
    r, g, b = hex_to_rgb(color)
    color_label.config(text=color, bg=color)
    root.config(bg=color)
    root.clipboard_clear()
    root.clipboard_append(color)
    status_label.config(text=f"Color {color} copied to clipboard!")
    rgb_label.config(text=f"R: {r}  G: {g}  B: {b}")

root = tk.Tk()
root.title("Random Color Picker")
root.geometry("400x300")

color_label = tk.Label(root, text="", font=("Arial", 30), width=10)
color_label.pack(pady=20)

rgb_label = tk.Label(root, text="", font=("Arial", 16))
rgb_label.pack()

pick_button = tk.Button(root, text="Pick a Random Color", command=pick_color, font=("Arial", 14))
pick_button.pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
status_label.pack()

root.mainloop()
