import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk
import sys

sys.path.append('tkinter' from 'c:\\Users\\melko\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\tkinter\\__init__.py'>)

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

greeting=tk.StringVar()

label=ttk.Label(root, padding=10, textvariable=greeting)
label.pack()

greeting.set('Hello, Mike!')


root.mainloop()