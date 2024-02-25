""" An object-oriented frame """

import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input=tk.StringVar()

        label=ttk.Label(self, text="Enter your name: ")
        entry=ttk.Entry(self, textvariable=self.user_input)
        button=ttk.Button(self, command=self.greet)

        label.pack(side='left')
        e.pack(side='left')
        label.pack(side='left')

    def greet(self):
        print(f'Hello {self.user_input.get()}!')    






root= tk.Tk()

frame=UserInputFrame(root)
label=ttk.Label(frame, text="Enter your name:")
label.pack()
frame.pack()

root.mainloop()