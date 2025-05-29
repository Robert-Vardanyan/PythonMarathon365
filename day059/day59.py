import tkinter as tk
from datetime import datetime, timedelta

def update_countdown():
    now = datetime.now()
    # Следующий Новый год — 1 января следующего года в 00:00:00
    next_year = datetime(year=now.year + 1, month=1, day=1)
    diff = next_year - now

    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    label.config(text=countdown_str)

    # Обновляем каждую секунду
    root.after(1000, update_countdown)

root = tk.Tk()
root.title("Countdown to New Year")

tk.Label(root, text="Time until New Year:", font=("Helvetica", 16)).pack(pady=10)
label = tk.Label(root, text="", font=("Helvetica", 24), fg="blue")
label.pack(pady=20)

update_countdown()
root.mainloop()
