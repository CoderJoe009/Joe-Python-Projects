import time
import webbrowser
import tkinter as tk
from tkinter import messagebox
from plyer import notification

class StudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Scheduler")
        
        self.schedule = [
            (8 * 60, 10 * 60, "Python"),
            (10 * 60 + 20, 11 * 60 + 20, "Math"),
            (11 * 60 + 35, 12 * 60 + 35, "Chemistry"),
            # ... add other subjects and times
        ]
        
        self.start_button = tk.Button(self.root, text="Start Study Schedule", command=self.start_schedule)
        self.start_button.pack()
        
    def start_timer(self, minutes, subject):
        time.sleep(minutes * 60)
        notification.notify(
            title="Study Reminder",
            message=f"It's time to study {subject}!",
            app_name="Study App",
        )
        
    def start_schedule(self):
        for start, end, subject in self.schedule:
            remaining_time = end - int(time.time() / 60)
            if remaining_time > 0:
                notification.notify(
                    title="Study Timer Started",
                    message=f"Starting {subject} study session.",
                    app_name="Study App",
                )
                self.start_timer(remaining_time, subject)
                notification.notify(
                    title="Study Session Ended",
                    message=f"{subject} study session completed.",
                    app_name="Study App",
                )
            else:
                messagebox.showinfo("Session Already Completed", f"{subject} study session already completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyApp(root)
    root.mainloop()
