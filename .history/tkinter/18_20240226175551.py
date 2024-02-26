import tkinter as tk

def close_window():
    parent.destroy()

parent=tk.Tk()
parent.title("Close window example")

label=tk.Label(parent, text="Click the 'Close' button to close this window")