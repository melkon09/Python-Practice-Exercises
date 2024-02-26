import tkinter as tk

# Function to update the calculator display
def update_display(value):
    current_text = display.get()
    new_text = current_text + value
    display.set(new_text)

# Function to calculate and display the result
def calculate_result(*args):
    try:
        result = eval(display.get())
        display.set(str(result))
    except Exception as e:
        display.set("Error")

# Function to clear the calculator display
def clear_display(*args):
    display.set("")

# Create the main Tkinter window
parent = tk.Tk()
parent.title("Calculator")

# Create a StringVar to store the display value
display = tk.StringVar()
display.set("")

# Create the calculator display Entry widget
display_entry = tk.Entry(parent, textvariable=display, font=("Arial", 18), justify="right")
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Define the button labels for digits, operators, and special functions
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

# Create and arrange the buttons in a grid
row_val = 1
col_val = 0

for label in button_labels:
    if label == '=':
        tk.Button(parent, text=label, padx=20, pady=20, font=("Arial", 16), command=calculate_result).grid(row=row_val, column=col_val)
    elif label == 'C':
        tk.Button(parent, text=label,bg='darkred',activebackground='red', activeforeground= fg='white', padx=20, pady=20, font=("Arial", 16), command=clear_display).grid(row=row_val, column=col_val)
    else:
        tk.Button(parent, text=label, padx=20, pady=20, font=("Arial", 16), command=lambda l=label: update_display(l)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

parent.bind("<Escape>", clear_display)
# Run the Tkinter main loop
parent.mainloop()
