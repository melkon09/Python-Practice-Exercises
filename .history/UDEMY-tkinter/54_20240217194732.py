import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

image=Image.open('C:/Users/melko/OneDrive/Documents/GitHub/Python-Practice-Exercises/UDEMY-tkinter/Python-logo-notext.svg.png')
photo = ImageTk.PhotoImage(image)
label=ttk.Label(root, image=photo, padding=5, fill='true')
label.pack()

root.mainloop()