import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

initial_value=tk.StringVar(value=20)
spin_box = ttk.Spinbox(
    root,
    
    textvariable=initial_value,
    wrap=False  # if true, loops to the minimum value after reaching the max
)

spin_box.pack()

print(spin_box.get())

root.mainloop()