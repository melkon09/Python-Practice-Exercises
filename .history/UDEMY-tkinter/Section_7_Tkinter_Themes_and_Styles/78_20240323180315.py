'''Tkinter themes, and how to change theme'''

import tkinter as tk
from tkinter import ttk



def greet(*args):
    print(f'Hello, {user_name.get()}!')


root=tk.Tk()
root.resizable(False, False)
root.title("Greeter")


main=ttk.Frame(root, padding=(40, 20))
