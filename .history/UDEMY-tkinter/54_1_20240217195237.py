import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()


root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

greeting=tk.StringVar()

label=ttk.Label(root, padding=)

image=Image.open('C:/Users/melko/OneDrive/Documents/GitHub/Python-Practice-Exercises/UDEMY-tkinter/Python-logo-notext.svg.png').resize((400, 400))
photo = ImageTk.PhotoImage(image)
label=ttk.Label(root, text='Image with text', image=photo, padding=5, compound='center')
label.pack()



root.mainloop()