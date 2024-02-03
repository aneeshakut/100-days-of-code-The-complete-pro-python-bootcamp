#Stop Watch of 25min

import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.time_remaining = 1500  # 25 minutes in seconds
        self.is_running = False

        self.label = tk.Label(master, text=self.format_time())
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def format_time(self):
        minutes, seconds = divmod(self.time_remaining, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer(self):
        if self.is_running:
            self.time_remaining -= 1
            self.label.config(text=self.format_time())

            if self.time_remaining <= 0:
                self.stop_timer()
                messagebox.showinfo("Pomodoro Timer", "Time's up! Take a break.")

        self.master.after(1000, self.update_timer)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

            # Reset timer to 25 minutes
            self.time_remaining = 1500
            self.label.config(text=self.format_time())

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()
