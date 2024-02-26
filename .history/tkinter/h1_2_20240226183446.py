import tkinter as tk

parent=tk.Tk()
parent.title("Widgets with Grid")

label1=tk.Label(parent, text="Label 1", bg="lightblue")
label2=tk.Label(parent, text='Label 2', bg="lightgreen")
label3=tk.Label(parent, text="Label 3", bg="lightyellow")
button=tk.Button(parent, text="Click me!")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, columnspan=2)