import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        # Get the value from the input field
        value = float(entry.get())
        
        # Check which units are selected and perform conversion
        if unit_from.get() == "Meters" and unit_to.get() == "Kilometers":
            result = value / 1000
        elif unit_from.get() == "Kilometers" and unit_to.get() == "Meters":
            result = value * 1000
        elif unit_from.get() == "Grams" and unit_to.get() == "Kilograms":
            result = value / 1000
        elif unit_from.get() == "Kilograms" and unit_to.get() == "Grams":
            result = value * 1000
        else:
            result = value  # if units are the same
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x350")  # Set window size (width x height)
window.config(padx=20, pady=20)  # Add padding inside the window

# Set a more modern font and color scheme
label_font = ('Helvetica', 14)
button_font = ('Helvetica', 12)

# Label and input field
label = tk.Label(window, text="Enter value:", font=label_font)
label.pack(pady=10)

entry = tk.Entry(window, font=('Helvetica', 14))
entry.pack(pady=10, fill="x")

# Dropdowns for unit selection
unit_from = tk.StringVar(window)
unit_from.set("Meters")  # default value
unit_to = tk.StringVar(window)
unit_to.set("Kilometers")

unit_menu_from = tk.OptionMenu(window, unit_from, "Meters", "Kilometers", "Grams", "Kilograms")
unit_menu_from.config(width=15, font=button_font)
unit_menu_from.pack(pady=10)

unit_menu_to = tk.OptionMenu(window, unit_to, "Meters", "Kilometers", "Grams", "Kilograms")
unit_menu_to.config(width=15, font=button_font)
unit_menu_to.pack(pady=10)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert, font=button_font, bg='#4CAF50', fg='white', relief='raised')
convert_button.pack(pady=20)

# Result label
result_label = tk.Label(window, text="Result:", font=('Helvetica', 14))
result_label.pack(pady=10)

# Run the main loop
window.mainloop()
