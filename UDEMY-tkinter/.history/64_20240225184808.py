import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.title("Distance converter")

main =ttk.Frame(root, padding=(30, 15))
main.grid()

meters_label=ttk.Label(main, text="Meters:")
meters_input=ttk.Entry(main, width=10)
feet_label=ttk.Label(main, text="Feet:")
feet_display=ttk.Label(main, text="Feet shown here")
calc_button=ttk.Button(main, text="Calculate")

meters_label.grid(column=0, row=0, sticky="W", padx=5, pady)
meters_input.grid(column=1, row=0, sticky="EW")
meters_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

root.mainloop()