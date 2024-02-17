import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

label=ttk.Label(root, text="Hello, world!", padding=20)
label.config(font)
label.pack()

root.mainloop()