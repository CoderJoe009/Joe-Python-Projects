import time
from plyer import notification

# Define the schedule with session names and timings
schedule = [
    ("Maths", "8:00 AM", "8:25 AM"),
    ("Python", "8:40 AM", "9:05 AM"),
    ("Physics", "9:20 AM", "10:55 AM"),
    ("CS", "11:20 AM", "11:55 AM"),
    ("Geography", "12:10 PM", "12:35 PM"),
    ("Lunch Break", "12:50 PM", "2:00 PM"),
    ("English", "2:00 PM", "2:25 PM"),
    ("Swahili", "2:40 PM", "3:05 PM"),
    ("Chemistry", "3:20 PM", "3:55 PM"),
    ("Biology", "4:10 PM", "4:35 PM"),
    ("Maths", "4:50 PM", "5:15 PM"),
    ("Python", "5:30 PM", "5:55 PM")
]

# Convert time strings to time objects
def convert_to_time(time_str):
    return time.strptime(time_str, "%I:%M %p")

# Main loop
for session, start_time_str, end_time_str in schedule:
    start_time = convert_to_time(start_time_str)
    end_time = convert_to_time(end_time_str)
    
    while True:
        current_time = time.localtime()
        
        if start_time <= current_time <= end_time:
            notification_title = "Session Reminder"
            notification_message = f"{session} session is starting now!"
            break
        
        time.sleep(60)  # Check every 1 minute
    
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10
    )
