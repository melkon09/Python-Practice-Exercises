import tkinter as tk

parent=tk.Tk()
parent.title("tkinter exercise")
my_label=tk.Label(parent, text = "Hello", font=("Arial Bold", 70))
my_label.grid(column = 3, row=3)
parent.mainloop()