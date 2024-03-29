""" Finishing our Object-Oriented HelloWorld app """

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
        button=ttk.Button(self, command=self.greet, text="Press me!")
        entry.focus()

        label.pack(side='left')
        entry.pack(side='left')
        button.pack(side='left')

    def greet(self):
        print((f'Hello {self.user_input.get()}!') if self.user_input else 'Hello stranger!')    




root= tk.Tk()
frame=UserInputFrame(root)
frame.pack()


root.mainloop()