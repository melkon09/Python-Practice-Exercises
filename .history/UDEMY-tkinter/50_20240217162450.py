import tkinter as tk
from tkinter import ttk

def greet():
    print(f'Hello, {user_name.get() or 'World'}!')



root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()

