import tkinter as tk
import random
import string
import pyperclip


root=tk.Tk()
root.title("Password Generator")
root.geometry('225x100')

root_color='peachpuff'

root.config(bg=root_color)

def generate():
    password=""
    digits=string.digits
    characters="!@#$%^&*()"
    lower_alphabets=string.ascii_lowercase
    upper_alphabets=string.ascii_uppercase
    