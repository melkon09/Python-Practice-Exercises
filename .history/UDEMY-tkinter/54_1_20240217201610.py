import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

sys.path.append('c:/users/melko/appdata/local/packages/pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0/localcache/local-packages/python312/site-packages (10.2.0)')
from PIL import Image, ImageTk
import sys



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