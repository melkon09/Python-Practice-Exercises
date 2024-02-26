import tkinter as tk

# Function to show tooltips
def show_tooltip(event, tooltip_text):
    tooltip.geometry(f'+{event.x_parent + 10}+{event.y_parent + 10}') # adjust tooltip position
    tooltip_label.config(text=tooltip_text)
    tooltip.deiconify()

# Function to hide tooltip
def hide_tooltip(event):
    tooltip.withdraw()

# Create the main window
