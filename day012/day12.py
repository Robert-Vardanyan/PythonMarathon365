import time
import sys

def countdown_timer(seconds):
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timeformat = f"{mins:02}:{secs:02}"
            sys.stdout.write(f"\r{timeformat}")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        sys.stdout.write("\r00:00\n")
        print("\nTime's up!")
    except KeyboardInterrupt:
        print("\nTimer was interrupted.")

# Input the time for the timer (in seconds)
seconds = int(input("Enter the number of seconds for the timer: "))
countdown_timer(seconds)
