import tkinter as tk
from tkinter import Menu

# Create the main window
parent= tk.Tk()
parent.title('Spyder (Python 3.6)')

# Create a menu bar
menu_bar=Menu(parent)
parent.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label='New')
