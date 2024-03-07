import tkinter as tk
import ran

root=tk.Tk()
root.title("Password Generator")
root.geometry('225x100')

root_color='peachpuff'

root.config(bg=root_color)

def generate():
    password=""
    digits=string.digits
