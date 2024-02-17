import tkinter as tk
from tkinter import ttk

def greet():
    print(f'Hello, {user_name.get() or 'World'}!')



root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()


name_label = ttl.name_label(root, text='Name: ')
name_label.pack(side='Left', padx=(0, 10))
name_entry = ttk.Entry