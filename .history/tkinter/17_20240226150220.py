import tkinter as tk

# Function to show tooltips
def show_tooltip(event, tooltip, tooltip_text):
    tooltip.geometry(f"+{event.x.parent + 10}+{event.y _parent + 10}") # adjust tooltip position
    tooltip_label.config(text=tooltip_text)
    tooltip.deiconify()

# Function to hide tooltip
def hide_tooltip(event):
    tooltip.withdraw()

# Create the main window
parent=tk.Tk()
parent.title("Tooltip Example")

# Create a button with a tooltip
button = tk.Button(parent, text="Button with tooltip")
button.pack(padx=10, pady=10)
button.bind("<Enter>", lambda event :show_tooltip(event, tooltip, "This is a button."))
button.bind("<Leave>", hide_tooltip)

# Create a label with a tooltip
label=tk.Label(parent, text="Label with a tooltip")
label.pack(padx=10, pady=10)
label.bind("<Enter>", lambda event :show_tooltip(event, tooltip, "This is a label."))
label.bind("<Leave>", hide_tooltip)

# Create the tooltip window (Hidden by default)
tooltip = tk.Toplevel(parent)
tooltip.withdraw()
tooltip_label=tk.Label(tooltip, text="", background ="lightyellow", relief = "solid", borderwidth=1)
tooltip_label.pack()

# Start the Tkinter event loop
parent.mainloop()