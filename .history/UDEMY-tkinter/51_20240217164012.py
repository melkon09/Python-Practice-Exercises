import tkinter as tk
from tkinter import ttk


def greet():
    print(f'Hello, {user_name.get() or 'World'}!')


root = tk.Tk()          # Main window
root.title("Greeter")

user_name = tk.StringVar()

input_frame=ttk.Frame(root, padding=(20, 10, 20, 0)) # padding=(left, top, right, bottom)
input_frame.grid()

name_label = ttk.Label(input_frame, text='Name: ')
name_label.grid(side='left', padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(side='left')
name_entry.focus()

buttons=ttk.Frame(root, padding=(20, 10)) # padding=((left, right), (top, bottom))
buttons.grid(fill='both')

greet_button = ttk.Button(buttons, text='Greet', command=greet)
greet_button.grid(side="left", fill='x', expand='True')
quit_button = ttk.Button(buttons, text='Quit', command=root.destroy)
quit_button.grid(side='right', fill='x', expand='True')

root.mainloop()