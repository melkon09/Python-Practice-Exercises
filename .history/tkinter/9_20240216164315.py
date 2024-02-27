import tkinter as tk
from tkinter import messagebox

# Create the main window
parent=tk.Tk()
parent.title('Exercise 9- Messagebox')
parent.geometry("800x")

# Function to display a message in a messagebox
def show_message():
    messagebox.showinfo("Message", "Hello")

# Create a button to trigger the messagebox
button=tk.Button(parent, text="Show Message", command=show_message)
button.pack()

# Start the tkinter loop
parent.mainloop()