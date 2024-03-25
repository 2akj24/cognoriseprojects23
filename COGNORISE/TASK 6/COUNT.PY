import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.running = False
        self.paused = False
        
        self.label = tk.Label(master, font=("Arial", 24))
        self.label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Arial", 16))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", font=("Arial", 16), command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.pause_button = tk.Button(master, text="Pause", font=("Arial", 16), command=self.pause_resume_timer)
        self.pause_button.pack(side=tk.LEFT, padx=5, pady=10)

    def start_timer(self):
        if self.running and not self.paused:
            messagebox.showinfo("Timer", "Timer is already running!")
            return

        try:
            duration = int(self.entry.get())
            if duration <= 0:
                raise ValueError("Please enter a positive number.")

            self.running = True
            self.paused = False
            self.label.config(text="Timer started!")
            self.entry.config(state="disabled")
            self.start_button.config(text="Restart")

            while duration > 0 and self.running:
                if not self.paused:
                    self.label.config(text=f"Time left: {duration} seconds")
                    self.master.update()
                    time.sleep(1)
                    duration -= 1
                else:
                    time.sleep(0.1)

            if self.running:
                self.label.config(text="Time's up!")
                messagebox.showinfo("Timer", "Time's up!")
                self.entry.config(state="normal")
                self.entry.delete(0, tk.END)
                self.start_button.config(text="Start")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        
    def pause_resume_timer(self):
        if not self.running:
            messagebox.showinfo("Timer", "Timer is not running!")
            return
        
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")


def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
