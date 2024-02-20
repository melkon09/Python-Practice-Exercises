import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

langs= tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6)
langs_select


root.mainloop()