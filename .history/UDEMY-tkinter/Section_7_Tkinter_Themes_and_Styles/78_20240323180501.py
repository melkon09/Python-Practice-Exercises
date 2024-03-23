'''Tkinter themes, and how to change theme'''

import tkinter as tk
from tkinter import ttk



def greet(*args):
    print(f'Hello, {user_name.get()}!')


root=tk.Tk()
root.resizable(False, False)
root.title("Greeter")


main=ttk.Frame(root, padding=(40, 20))
main.grid()

user_name=tk.StringVar()

name_label = ttk.Label(main, text='Name:')
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row-0, column=)