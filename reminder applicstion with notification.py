from datetime import datetime, timedelta
from plyer import notification

def set_reminder(message, delay_minutes):
  """Sets a reminder with a notification after a delay in minutes.

  Args:
      message: The message content for the reminder.
      delay_minutes: The delay in minutes before showing the notification.
  """
  # Calculate reminder time
  reminder_time = datetime.now() + timedelta(minutes=delay_minutes)

  # Convert time to format suitable for plyer notification
  hour = reminder_time.hour
  minute = reminder_time.minute
  app_name = "Reminder"  # Customize app name

  # Schedule notification
  notification.notify(
      title=app_name,
      message=message,
      app_name=app_name,
      timeout=10,  # Notification timeout in seconds
      # Android options (optional, see plyer documentation)
      # ticker="Reminder!",
      # icon="icon.ico"  # Path to notification icon
  )

  print(f"Reminder set for '{message}' in {delay_minutes} minutes.")

# Example usage
message = "Take out the trash!"
delay_minutes = 1
set_reminder(message, delay_minutes)
