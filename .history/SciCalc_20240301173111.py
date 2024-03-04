import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("600x400")
root.resizable(False, False)

display_frame=tk.Frame(root, bg='red')
display_frame.pack()

button_frame=tk.Frame(root)
button_frame.grid()

root.mainloop()