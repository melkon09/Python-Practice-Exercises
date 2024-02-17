import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

image=Image.open('Python-logo-notext.svg.png')
photo = ImageTk.PhotoImage(image)
label=

label.pack()

root.mainloop()