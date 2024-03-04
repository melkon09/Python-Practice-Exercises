import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("600x400")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=10, pady=5, sticky="NEW")

tags={'n√x', '1/x', 'rad', 'deg', 'MC', 'MR', 'sin', 'arcsi'}

root.mainloop()