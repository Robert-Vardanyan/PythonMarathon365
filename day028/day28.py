import tkinter as tk
from tkinter import messagebox


class NumberBaseConverter:
    def __init__(self):
        pass

    # Convert to binary
    def to_binary(self, number):
        return bin(number)[2:]

    # Convert to octal
    def to_octal(self, number):
        return oct(number)[2:]

    # Convert to hexadecimal
    def to_hexadecimal(self, number):
        return hex(number)[2:].upper()

    # Convert from string to decimal
    def to_decimal(self, number_str, base):
        try:
            return int(number_str, base)
        except ValueError:
            return None


class NumberBaseConverterGUI:
    def __init__(self, root):
        self.converter = NumberBaseConverter()

        # Set up the main window
        self.root = root
        self.root.title("Number Base Converter")
        self.root.geometry("400x400")

        # Create a frame for centering the elements
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Label for input
        self.input_label = tk.Label(self.frame, text="Enter Decimal Number:")
        self.input_label.pack(pady=5)

        # Input field with increased size
        self.input_entry = tk.Entry(self.frame, width=25, font=("Arial", 14))
        self.input_entry.pack(pady=5)

        # Buttons for conversion
        self.binary_button = tk.Button(self.frame, text="Convert to Binary", command=self.convert_to_binary, width=20, height=2, bg='lightblue')
        self.binary_button.pack(pady=5)

        self.octal_button = tk.Button(self.frame, text="Convert to Octal", command=self.convert_to_octal, width=20, height=2, bg='lightgreen')
        self.octal_button.pack(pady=5)

        self.hex_button = tk.Button(self.frame, text="Convert to Hexadecimal", command=self.convert_to_hexadecimal, width=20, height=2, bg='lightcoral')
        self.hex_button.pack(pady=5)

        # Label and result display
        self.result_label = tk.Label(self.frame, text="Result:")
        self.result_label.pack(pady=5)

        self.result_value = tk.Label(self.frame, text="", font=("Arial", 14))
        self.result_value.pack(pady=5)

    def convert_to_binary(self):
        try:
            decimal_number = int(self.input_entry.get())
            result = self.converter.to_binary(decimal_number)
            self.result_value.config(text=f"Binary: {result}", fg="blue")
        except ValueError:
            self.show_error("Please enter a valid decimal number.")

    def convert_to_octal(self):
        try:
            decimal_number = int(self.input_entry.get())
            result = self.converter.to_octal(decimal_number)
            self.result_value.config(text=f"Octal: {result}", fg="green")
        except ValueError:
            self.show_error("Please enter a valid decimal number.")

    def convert_to_hexadecimal(self):
        try:
            decimal_number = int(self.input_entry.get())
            result = self.converter.to_hexadecimal(decimal_number)
            self.result_value.config(text=f"Hexadecimal: {result}", fg="red")
        except ValueError:
            self.show_error("Please enter a valid decimal number.")

    def show_error(self, message):
        messagebox.showerror("Input Error", message)


if __name__ == "__main__":
    root = tk.Tk()
    gui = NumberBaseConverterGUI(root)
    root.mainloop()
