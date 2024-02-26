import tkinter as tk
import time
# Function to update the labe text with the current time
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)   # Update every 1000 milliseconds
# Create the main window
root=tk.Tk()
root.title("Digital Clock")
# Create a label to display the time
clock_label=tk.Label(root, text="", font=("Helvetica", 48))
clock_label.pack()    