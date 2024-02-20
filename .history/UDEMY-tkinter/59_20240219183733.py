import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

storage_variable=StringVar()

option_one=ttk.Radiobutton(
    root,
    text='Option 1',
    variable=storage_variable,
    value="First option"
)


root.mainloop()