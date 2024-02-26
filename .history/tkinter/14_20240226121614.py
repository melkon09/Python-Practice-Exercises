import tkinter as tk
import time
# Function to update the labe text with the current time
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time) 