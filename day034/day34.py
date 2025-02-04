import tkinter as tk
from tkinter import ttk


def rgb_to_hex(r, g, b):
    """Преобразование RGB в Hex."""
    return f"{r:02x}{g:02x}{b:02x}"


def hex_to_rgb(hex_value):
    """Преобразование Hex в RGB."""
    hex_value = hex_value.lstrip('#')
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))


def update_color():
    """Обновление фона, значений RGB и Hex при изменении ползунков."""
    try:
        r = int(red_slider.get())
        g = int(green_slider.get())
        b = int(blue_slider.get())
        hex_value = rgb_to_hex(r, g, b)
    except ValueError:
        hex_value = "000000"
        r, g, b = 0, 0, 0
    
    # Обновление цвета
    color_display.config(bg=f"#{hex_value}")

    # Обновление значений Hex и RGB
    hex_label.config(text=f"Hex: {hex_value.upper()}")
    rgb_label.config(text=f"RGB: {r}, {g}, {b}")


def copy_hex():
    """Копировать Hex в буфер обмена без #."""
    hex_value = hex_label.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(hex_value)


def copy_rgb():
    """Копировать RGB в буфер обмена как цифры, без текста."""
    rgb_value = rgb_label.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(rgb_value)


# Создание окна
root = tk.Tk()
root.title("Color Mixer (RGB to Hex Converter)")
root.geometry("400x420")

# Окно для отображения выбранного цвета
color_display = tk.Label(root, width=30, height=8, bg="#ffffff", relief="sunken")
color_display.pack(pady=20)

# Ползунки для выбора значений RGB
red_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Red", command=lambda x: update_color())
red_slider.pack(fill="x", padx=20)
red_slider.config(fg="red")

green_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Green", command=lambda x: update_color())
green_slider.pack(fill="x", padx=20)
green_slider.config(fg="green")

blue_slider = tk.Scale(root, from_=0, to=255, orient="horizontal", label="Blue", command=lambda x: update_color())
blue_slider.pack(fill="x", padx=20)
blue_slider.config(fg="blue")

# Лейблы для отображения Hex и RGB значений
hex_label_frame = tk.Frame(root)
hex_label_frame.pack(pady=5, fill="x")

hex_label = tk.Label(hex_label_frame, text="Hex: 000000", font=("Arial", 12))
hex_label.pack(side="left", padx=5)

copy_hex_button = tk.Button(hex_label_frame, text="Copy Hex", command=copy_hex)
copy_hex_button.pack(side="right", padx=5)

rgb_label_frame = tk.Frame(root)
rgb_label_frame.pack(pady=5, fill="x")

rgb_label = tk.Label(rgb_label_frame, text="RGB: 0, 0, 0", font=("Arial", 12))
rgb_label.pack(side="left", padx=5)

copy_rgb_button = tk.Button(rgb_label_frame, text="Copy RGB", command=copy_rgb)
copy_rgb_button.pack(side="right", padx=5)

# Инициализация с начальным цветом
update_color()

# Запуск основного цикла
root.mainloop()
