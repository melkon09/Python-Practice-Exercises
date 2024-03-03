""" Adding an inner container for our frames """

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from windows import set_dpi_awareness

set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")

        container=ttk.Frame(self)
        container.grid(padx=60, pady=30)

        frame=MetersToFeet(self, padding=(30, 10))
        frame.grid()

        self.bind("<Return>", frame.calculate_feet)
        self.bind("<KP_Enter>", frame.calculate_feet)

class MetersToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.meters_value=tk.StringVar()
        self.feet_value=tk.StringVar(value="Feet shown here.")
        
        meters_label=ttk.Label(self, text="Meters:")
        meters_input=ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Segoe UI", 12))
        feet_label=ttk.Label(self, text="Feet:")
        feet_display=ttk.Label(self, textvariable=self.feet_value)
        calc_button=ttk.Button(self, text="Calculate", command=self.calculate_feet)

        meters_label.grid(column=0, row=0, sticky="W")
        meters_input.grid(column=1, row=0, sticky="EW")
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=5)


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
root.mainloop()