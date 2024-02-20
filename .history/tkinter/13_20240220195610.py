import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression and display the result
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")

# Create the main window
parent= tk.Tk()
parent.title("Calculator")

# Create a variable to store current display value
display_var = tk.StringVar()
display_var.set("0")

# Create the display label
display_label=tk.Label(
    parent,
    textvariable=display_var,
    font=("Arial", 24),
    anchor="e",
    bg="lightgray",
    padx=10,
    pady=10,
    )
display_label.grid(row=0, column=0, columnspan=4)

# Define the button layout
button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("7", 1, 3),
    ("7", 1, 0), ("7", 1, 0), ("7", 1, 0), ("7", 2, 3),
    ("7", 1, 0), ("7", 1, 0), ("7", 1, 0), ("7", 1, 3),
    ("7", 1, 0), ("7", 1, 0), ("7", 1, 0), ("7", 1, 3), 
]