import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("600x400")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

di=tk.Entry(frame)
input.grid(padx=10, pady=5, sticky="NEW")

root.mainloop()