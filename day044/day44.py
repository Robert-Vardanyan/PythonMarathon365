import tkinter as tk
from tkinter import ttk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱️ Simple Stopwatch")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.time_label = ttk.Label(root, text="00:00:00", font=("Courier", 40))
        self.time_label.pack(pady=20)

        self.start_button = ttk.Button(root, text="▶ Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.stop_button = ttk.Button(root, text="⏹ Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.reset_button = ttk.Button(root, text="🔁 Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, expand=True, padx=10)

        self.running = False
        self.start_time = None
        self.elapsed = 0

    def update_time(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            mins, secs = divmod(self.elapsed, 60)
            hours, mins = divmod(mins, 60)
            time_str = f"{int(hours):02}:{int(mins):02}:{int(secs):02}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.time_label.config(text="00:00:00")

def main():
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
