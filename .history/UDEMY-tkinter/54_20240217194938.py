import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

image=Image.open('C:/Users/melko/OneDrive/Documents/GitHub/Python-Practice-Exercises/UDEMY-tkinter/Python-logo-notext.svg.png').resize((400, 400))
photo = ImageTk.PhotoImage(image)
label=ttk.Label(root, text=image=photo, padding=5)
label.pack()



root.mainloop()