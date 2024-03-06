""" Adding keybindings to the project """

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from windows import set_dpi_awareness

set_dpi_awareness()

class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.frames=dict()

        container=ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")
 
        #self.bind("<Return>", frame.calculate)
        #self.bind("<KP_Enter>", frame.calculate)

        for FrameClass in (MetersToFeet, FeetToMeters):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky='NSEW')

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>",frame.calculate)
        self.bind("<KP_Enter", frame)
        frame.tkraise()

class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.meters_value=tk.StringVar()
        self.feet_value=tk.StringVar(value="Feet shown here.")
        
        meters_label=ttk.Label(self, text="Meters:")
        meters_input=ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Segoe UI", 12))
        feet_label=ttk.Label(self, text="Feet:")
        feet_display=ttk.Label(self, textvariable=self.feet_value)
        calc_button=ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button=ttk.Button(
            self,
            text='Switch to feet conversion',
            command= lambda: controller.show_frame(FeetToMeters)
        )

        meters_label.grid(column=0, row=0, sticky="W")
        meters_input.grid(column=1, row=0, sticky="EW")
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=5)


    def calculate(self, *args):
        try:
            meters=float(self.meters_value.get())
            feet=meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            feet_value.set("Error")

class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value=tk.StringVar()
        self.meters_value=tk.StringVar(value="Meters shown here.")
        
        feet_label=ttk.Label(self, text="Feet:")
        feet_input=ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 12))
        meters_label=ttk.Label(self, text="Meters:")
        meters_display=ttk.Label(self, textvariable=self.meters_value)
        calc_button=ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button=ttk.Button(
            self,
            text='Switch to meters conversion',
            command= lambda: controller.show_frame(MetersToFeet)
        )

        feet_label.grid(column=0, row=0, sticky="W")
        feet_input.grid(column=1, row=0, sticky="EW")
        feet_input.focus()

        meters_label.grid(column=0, row=1, sticky="W")
        meters_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky='EW')   

        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=5)


    def calculate(self, *args):
        try:
            feet=float(self.feet_value.get())
            meters=feet / 3.28084
            self.meters_value.set(f"{meters:.3f}")
        except ValueError:
            self.meters_value.set("Error")            
root=DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=12)        # Extract from tkinter the default font that it is using for this application

root.columnconfigure(0,weight=1)
root.mainloop()