import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("600x400")
root.resizable(False, False)

display_frame=tk.Frame(root, bg='red', padx=5, pady=5)
display_frame.grid(sticky='NSEW')

frame=tk.Frame(root)
button_frame.grid()

display=tk.Entry(display_frame)
display_frame.grid()

root.mainloop()