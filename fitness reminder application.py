from datetime import datetime, timedelta
from plyer import notification

def set_reminder(message, time_str):
  """Sets a reminder with a notification for a specific time.

  Args:
      message: The message content for the reminder.
      time_str: Time in 24-hour format (HH:MM) or relative time like "in 30m".
  """
  # Parse time string
  try:
    # Check for 24-hour format
    hour, minute = map(int, time_str.split(":"))
  except ValueError:
    # Try parsing relative time (assumes minutes)
    time_value, unit = time_str.split()
    delay_minutes = int(time_value)
    if unit.lower() == "m":
      # Minutes
      pass
    elif unit.lower() == "h":
      # Convert hours to minutes
      delay_minutes *= 60
    else:
      raise ValueError("Invalid time unit. Use 'm' for minutes or 'h' for hours.")

    # Calculate reminder time based on relative delay
    reminder_time = datetime.now() + timedelta(minutes=delay_minutes)
  else:
    # Valid 24-hour format, check for time in the past
    current_time = datetime.now()
    reminder_time = datetime.strptime(f"{datetime.now().date()} {time_str}", "%Y-%m-%d %H:%M")
    if reminder_time < current_time:
      raise ValueError("Time cannot be in the past. Use relative time for future reminders.")

  # Calculate delay in minutes for plyer
  delay_minutes = int((reminder_time - datetime.now()).total_seconds() / 60)

  # Schedule notification
  notification.notify(
      title="Fitness Reminder",
      message=message,
      app_name="Fitness Reminder",
      timeout=10,  # Notification timeout in seconds
  )

  print(f"Reminder set for '{message}' at {time_str}.")

# Example usage
message = "Time for your workout!"
# Set reminder for specific time (8:30 AM)
time_str = "08:30"
# set_reminder(message, time_str)

# Set reminder with relative time (in 45 minutes)
time_str = "in 45m"
set_reminder(message, time_str)
