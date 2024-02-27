import tkinter as tk
from Pillow import Image, ImageTk

parent-tk.Tk()
parent.title("Image in Tkinter")

image=Image.open('C:/Users/melko/OneDrive/Pictures/EAP.png')
image=ImageTk.PhotoImage(image)

image_label=tk.Label(parent, image=image)
image_label.pack()

parent.mainloop()