import time
from datetime import datetime

# Function to get the birthday date from the user
def get_birthday():
    print("Enter your birth date in the format (day.month.year):")
    birthday_str = input()
    birthday = datetime.strptime(birthday_str, "%d.%m.%Y")
    return birthday

# Function to countdown time to the birthday
def countdown(birthday):
    while True:
        now = datetime.now()
        # Check if the birthday has already passed this year; if so, countdown to the next year
        if now.month > birthday.month or (now.month == birthday.month and now.day > birthday.day):
            birthday = birthday.replace(year=now.year + 1)

        # Calculate the remaining time
        delta = birthday - now
        days_left = delta.days
        hours_left = delta.seconds // 3600
        minutes_left = (delta.seconds // 60) % 60
        seconds_left = delta.seconds % 60

        # Display the result
        print(f"Time left: {days_left} days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds.")
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    birthday = get_birthday()  # Get the birthday date
    countdown(birthday)  # Start the countdown
