import tkinter as tk
import random
import string
import pyperclip
import time

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
    main_string=digits+characters+lower_alphabets+upper_alphabets
    main_list=list(main_string)
    random.seed()
    random.shuffle(main_list)

    random_len=random.randint(8,15)