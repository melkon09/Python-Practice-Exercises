import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

initial_value=tk.IntVar(value=20)
spin_box = tk.Spinbox(
    root,
    from_=0,
    to
)





root.mainloop()