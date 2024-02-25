""" An object-oriented frame """

import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

class HelloWorld(tk.Tk):    # The HelloWorld class inherits from tk.Tk
    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        ttk.Label(self, text="Hello World!").pack()



root= HelloWorld()

root.mainloop()