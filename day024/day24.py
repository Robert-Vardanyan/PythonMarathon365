import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        
        self.running = False
        self.time = 0
        
        # Label for time display
        self.time_label = tk.Label(self.root, text="0.0", font=("Helvetica", 30), width=10)
        self.time_label.pack(pady=20)
        
        # Start/Stop button
        self.start_stop_button = tk.Button(self.root, text="Start", font=("Helvetica", 14), width=10, command=self.start_stop)
        self.start_stop_button.pack(pady=10)
        
        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 14), width=10, command=self.reset)
        self.reset_button.pack(pady=10)
        
        self.update_time()

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_stop_button.config(text="Start")
        else:
            self.running = True
            self.start_stop_button.config(text="Stop")
            self.update_time()

    def reset(self):
        self.time = 0
        self.time_label.config(text="0.0")
        
    def update_time(self):
        if self.running:
            self.time += 0.1
            self.time_label.config(text=f"{self.time:.1f}")
            self.root.after(100, self.update_time)

# Create the main window
root = tk.Tk()

# Create the Stopwatch instance
stopwatch = Stopwatch(root)

# Start the Tkinter event loop
root.mainloop()
