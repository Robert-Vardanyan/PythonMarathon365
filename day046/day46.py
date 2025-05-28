import tkinter as tk

class FlashlightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashlight")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.is_on = False

        # Цвет фона окна - чёрный изначально
        self.root.configure(bg="black")

        # Создаём Canvas с таким же фоном, чтобы "прозрачный" эффект
        self.canvas = tk.Canvas(root, width=150, height=150, bg="black", highlightthickness=0)
        self.canvas.pack(expand=True)

        # Рисуем круг (овал с равными сторонами)
        self.circle = self.canvas.create_oval(5, 5, 145, 145, fill="white", outline="", width=0)

        # Текст внутри круга
        self.text = self.canvas.create_text(75, 75, text="Turn ON", font=("Arial", 16), fill="black")

        # Обрабатываем клик по кругу и тексту
        self.canvas.tag_bind(self.circle, "<Button-1>", self.toggle)
        self.canvas.tag_bind(self.text, "<Button-1>", self.toggle)

        self.update_color()

    def toggle(self, event=None):
        self.is_on = not self.is_on
        self.update_color()

    def update_color(self):
        if self.is_on:
            self.root.configure(bg="white")
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.circle, fill="lightgray")
            self.canvas.itemconfig(self.text, text="Turn OFF", fill="black")
        else:
            self.root.configure(bg="black")
            self.canvas.configure(bg="black")
            self.canvas.itemconfig(self.circle, fill="white")
            self.canvas.itemconfig(self.text, text="Turn ON", fill="black")

def main():
    root = tk.Tk()
    app = FlashlightApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
