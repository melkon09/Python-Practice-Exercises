""" Making the Distance Converter use OOP """

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from windows import set_dpi_awareness

set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Distance Converter")

        self.frame=ttk.Frame(self, padding=(30, 10))
        self.frame.grid()

class MetersToFeet(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.meters_value=tk.StringVar()
        self.feet_value=tk.StringVar(value="Feet shown here.")
        
        meters_label=ttk.Label(self, text="Meters:")
        meters_input=ttk.Entry(self, width=10, textvariable=meters_value, font=("Segoe UI", 12))
        feet_label=ttk.Label(root.frame, text="Feet:")
        feet_display=ttk.Label(root.frame, textvariable=feet_value)
        calc_button=ttk.Button(root.frame, text="Calculate", command=calculate_feet)


    def calculate_feet(self, *args):
        try:
            meters=float(self.meters_value.get())
            feet=meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            feet_value.set("Error")
            


root=DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=12)        # Extract from tkinter the default font that it is using for this application


root.columnconfigure(0,weight=1)


root. columnconfigure(0, weight=1)

# --  Widgets --


meters_label.grid(column=0, row=0, sticky="W")
meters_input.grid(column=1, row=0, sticky="EW")
meters_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in root.frame.winfo_children():
    child.grid_configure(padx=12, pady=5)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
