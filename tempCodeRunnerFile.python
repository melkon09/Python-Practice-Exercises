import tkinter as tk
from tkinter import ttk


def start_timer():
    global remaining_time
    try:
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        remaining_time = minutes*60 + seconds
        update_timer()
        start_button.config(state="disabled")
        stop_button.config(state="active")
    except ValueError:
        pass

def update_timer():
    global remaining_time
    if remaining_time>0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
        remaining_time-=1
        parent.after(1000, update_timer)
    else:
        timer_label.config(text="00:00")
        start_button.config(state="active")
        stop_button.config(state="disabled")           

def stop_timer():
    global remaining_time
    remaining_time = 0
    timer_label.config(text="00:00")
    start_button.config(state="active")
    stop_button.config(state="disabled")

parent = tk.Tk()
parent.title("Timer Application")

minutes_label = tk.Label(parent, text="Minutes:")
minutes_label.grid(row=0, column=0)
minutes_entry = tk.Entry(parent)
minutes_entry.grid(row=0, column=1)
minutes_entry.insert(0, "0")
seconds_label = tk.Label(parent, text="Seconds:")
seconds_label.grid(row=1, column=0)
seconds_entry = tk.Entry(parent)
seconds_entry.grid(row=1, column=1)
seconds_entry.insert(0, "0")
# Create and place timer label
timer_label = tk.Label(parent, text="00:00", font=("Helvetica", 48))
timer_label.grid(row=2, columnspan=2)
# Create and place start and stop buttons
start_button = ttk.Button(parent, text="Start", command=start_timer)
start_button.grid(row=3, column=0)
stop_button = ttk.Button(parent, text="Stop", command=stop_timer, state="disabled")
stop_button.grid(row=3, column=1)
# Initialize the remaining time
remaining_time = 0
# Start the Tkinter event loop
parent.mainloop()
