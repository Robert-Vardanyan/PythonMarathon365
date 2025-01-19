import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import time
import threading
import simpleaudio as sa

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x350")
        self.root.configure(bg="#f5f5dc")

        # Title
        tk.Label(root, text="Alarm Clock", font=("Arial", 24, "bold"), bg="#f5f5dc", fg="#2b2b2b").pack(pady=10)

        # Labels and input fields for time
        self.time_frame = tk.Frame(root, bg="#f5f5dc")
        self.time_frame.pack(pady=10)

        self.hours_label = tk.Label(self.time_frame, text="Hours", font=("Arial", 12), bg="#f5f5dc")
        self.hours_label.grid(row=0, column=0, padx=5)
        self.minutes_label = tk.Label(self.time_frame, text="Minutes", font=("Arial", 12), bg="#f5f5dc")
        self.minutes_label.grid(row=0, column=1, padx=5)
        self.seconds_label = tk.Label(self.time_frame, text="Seconds", font=("Arial", 12), bg="#f5f5dc")
        self.seconds_label.grid(row=0, column=2, padx=5)

        self.hours_entry = tk.Entry(self.time_frame, font=("Arial", 14), width=5, justify="center")
        self.hours_entry.grid(row=1, column=0, padx=5)
        self.minutes_entry = tk.Entry(self.time_frame, font=("Arial", 14), width=5, justify="center")
        self.minutes_entry.grid(row=1, column=1, padx=5)
        self.seconds_entry = tk.Entry(self.time_frame, font=("Arial", 14), width=5, justify="center")
        self.seconds_entry.grid(row=1, column=2, padx=5)

        # Set initial time value
        self.hours_entry.insert(0, "00")
        self.minutes_entry.insert(0, "00")
        self.seconds_entry.insert(0, "00")

        # Bind function to validate time input
        self.hours_entry.bind("<KeyRelease>", self.validate_time)
        self.minutes_entry.bind("<KeyRelease>", self.validate_time)
        self.seconds_entry.bind("<KeyRelease>", self.validate_time)

        # Set alarm button
        tk.Button(root, text="Set Alarm", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.set_alarm).pack(pady=10)

        # Label for displaying set time
        self.alarm_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5dc", fg="#2b2b2b")
        self.alarm_label.pack(pady=10)

        # Label for displaying time remaining
        self.time_remaining_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5dc", fg="#2b2b2b")
        self.time_remaining_label.pack(pady=10)

        self.alarm_time = None
        self.alarm_active = False
        self.alarm_playing = False

    def validate_time(self, event=None):
        # Get values from input fields
        hours = self.hours_entry.get().strip()
        minutes = self.minutes_entry.get().strip()
        seconds = self.seconds_entry.get().strip()

        # Correct the input for hours, minutes, and seconds
        try:
            hours = int(hours) if hours else 0
            minutes = int(minutes) if minutes else 0
            seconds = int(seconds) if seconds else 0

            # Limit values
            hours = min(max(hours, 0), 23)
            minutes = min(max(minutes, 0), 59)
            seconds = min(max(seconds, 0), 59)

            # Update input fields with corrected values
            self.hours_entry.delete(0, tk.END)
            self.minutes_entry.delete(0, tk.END)
            self.seconds_entry.delete(0, tk.END)
            self.hours_entry.insert(0, f"{hours:02}")
            self.minutes_entry.insert(0, f"{minutes:02}")
            self.seconds_entry.insert(0, f"{seconds:02}")
        except ValueError:
            pass  # Do nothing if there's an error during conversion

    def set_alarm(self):
        # Get time from input fields
        hours = self.hours_entry.get().strip()
        minutes = self.minutes_entry.get().strip()
        seconds = self.seconds_entry.get().strip()

        # If no time is entered, set alarm to 00:00:00
        if not hours or not minutes or not seconds:
            hours, minutes, seconds = "00", "00", "00"

        # Format time and validate
        try:
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)

            hours = hours % 24
            minutes = minutes % 60
            seconds = seconds % 60

            # Format the alarm time as HH:MM:SS
            alarm_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            self.alarm_time = alarm_time
            self.alarm_label.config(text=f"Alarm set for {alarm_time}")
            self.alarm_active = True
            self.start_alarm_thread()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid time in HH:MM:SS format")

    def start_alarm_thread(self):
        thread = threading.Thread(target=self.check_alarm)
        thread.daemon = True
        thread.start()

    def check_alarm(self):
        while self.alarm_active:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time == self.alarm_time and not self.alarm_playing:
                self.play_sound()
                break
            self.update_remaining_time()
            time.sleep(1)

    def play_sound(self):
        self.alarm_playing = True

        # Use simpleaudio to play the sound
        wave_obj = sa.WaveObject.from_wave_file("alarm.wav")  # Ensure the file exists
        play_obj = wave_obj.play()

        messagebox.showinfo("Alarm", "Time to wake up!")
    
        # Stop the sound after closing the message box
        play_obj.stop()

    def update_remaining_time(self):
        # Get current time and alarm time
        now = datetime.now()
        alarm_time = datetime.strptime(self.alarm_time, "%H:%M:%S")
        
        # Calculate remaining time
        if alarm_time > now:
            time_remaining = alarm_time - now
        else:
            # If time has passed, show the alarm will ring in 24 hours
            time_remaining = (alarm_time + timedelta(days=1)) - now

        # Remove days and milliseconds from the displayed time
        remaining_str = str(time_remaining).split()[2].split('.')[0]  # Use only time, without days and milliseconds
        self.root.after(1000, self.time_remaining_label.config, {'text': f"Time remaining: {remaining_str}"})

    def stop_alarm(self):
        self.alarm_active = False
        self.alarm_playing = False
        self.alarm_label.config(text="")
        self.time_remaining_label.config(text="")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
