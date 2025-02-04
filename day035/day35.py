import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageDraw

class SimpleDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        self.root.geometry("500x500")
        
        self.canvas = tk.Canvas(self.root, bg="white", width=500, height=400)
        self.canvas.pack()

        self.drawing = False
        self.last_x, self.last_y = None, None
        self.color = "black"  # Стартовый цвет для рисования

        self.create_ui()

        # Создаем изображение для сохранения
        self.image = Image.new("RGB", (500, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def create_ui(self):
        # Кнопка для выбора цвета в верхнем правом углу
        self.color_button = tk.Button(self.root, text="Color", command=self.choose_color)
        self.color_button.place(x=450, y=10)

        # Контейнер для кнопок "Clear" и "Save"
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(fill=tk.X, padx=10, pady=10)

        # Кнопка очистки
        self.clear_button = tk.Button(buttons_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, expand=True)

        # Кнопка сохранения
        self.save_button = tk.Button(buttons_frame, text="Save", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, expand=True)

        # Настроим подписи для инструкций
        self.instructions_label = tk.Label(self.root, text="Use the mouse to draw. Press 'Clear' to reset.")
        self.instructions_label.pack(side=tk.BOTTOM, pady=10)

        # Привяжем события мыши
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def start_drawing(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            # Рисуем символы на холсте
            self.canvas.create_text(event.x, event.y, text="*", font=("Courier", 10), fill=self.color)
            
            # Рисуем на изображении для сохранения
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.color, width=1)

            self.last_x, self.last_y = event.x, event.y

    def stop_drawing(self, event):
        self.drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")
        # Очищаем изображение для следующего рисования
        self.image = Image.new("RGB", (500, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def choose_color(self):
        # Открыть диалог выбора цвета
        color = askcolor()[1]
        if color:
            self.color = color

    def save_image(self):
        # Сохранение изображения
        file_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleDrawingApp(root)
    root.mainloop()
