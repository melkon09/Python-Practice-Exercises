import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

def hand

scale =ttk.Scale(root, orient="horizontal", from_=0, to=10)
scale.pack(fil="x")




root.mainloop()