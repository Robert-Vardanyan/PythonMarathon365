from plyer import notification
import time

# Notification with enhanced styling
def show_notification():
    notification.notify(
        title='Important Notification!',
        message='This is a test notification from Project 10.',
        timeout=10,  # Duration of the notification (in seconds)
        app_name='Example App',  # The name of the application
        ticker='Notification received!',  # The message that appears in the taskbar
        toast=False  # Disable toast notifications on some OS
    )

    # You can add additional logic or delay if needed
    time.sleep(1)

show_notification()
