import time
from plyer import notification

def water_reminder(interval_hours=1):
    """
    Sends a desktop notification to remind you to drink water.
    :param interval_hours: Interval in hours for the reminders (default is 1 hour).
    """
    interval_seconds = interval_hours * 3600  # Convert hours to seconds
    
    while True:
        notification.notify(
            title="💧 Hydration Reminder 💧",
            message="It's time to drink a glass of water!",
            timeout=6  # Notification duration in seconds
        )
        time.sleep(interval_seconds)

# Example usage: remind every hour
water_reminder(1)
