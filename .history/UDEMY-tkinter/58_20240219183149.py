import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())

check=Checkbutton(
    root,
    text="Check Example",
    variable=selected_option,
    command=print_current_option,
    on
)    

root.mainloop()