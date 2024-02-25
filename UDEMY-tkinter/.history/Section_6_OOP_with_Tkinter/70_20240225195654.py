""" Creating a class for our app window """
import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

class HelloWorld(tk.Tk):    # The HelloWorld class inherits from tk.Tk
    def __


root= HelloWorld()

root.mainloop()