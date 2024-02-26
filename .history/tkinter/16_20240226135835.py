import tkinter as tk
from tkinter import messagebox

def validate_login():
    username=username_entry.get()
    password=password_entry.get()

    if username==



parent=tk.Tk()
parent.title("Login Form")

username_label = tk.Label(parent, text="User ID")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

password_label = tk.Label(parent, text="Password")
password_label.pack()

password_entry = tk.Entry(parent)
password_entry.pack()

login_button=tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

parent.mainloop()