import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget examples")

selected_weekday=tk.StringVar()
weekday=ttk.Combobox(root, textvariable=selected_weekday)
weekday['values'] = ('Monday','Tuesday','Wednesday','Thursday','Friday')
weekday['state']= 'readonly' # 'normal'
weekday.pack()

def handle_selection(event):
    print('Today is', selected_weekday.get())
    print("But we 're gonna change it to Friday.")
root.mainloop()