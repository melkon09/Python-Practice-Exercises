import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

image=Image.openF
label=ttk.Label(root, image=photo, padding=5)
label.pack()

root.mainloop()