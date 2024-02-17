import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

label=ttk.Label(root, text="Hello, world!", padding=20)
label.config(font=("Segoe UI", 20))
label.pack()


root.mainloop()