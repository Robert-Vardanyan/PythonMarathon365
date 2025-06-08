import threading

def alert():
    print("Timer Alert!")
    # Schedule the next alert in 5 seconds
    threading.Timer(5, alert).start()

# Start the first alert
alert()

# Keep the main thread alive so the alerts continue
while True:
    pass
