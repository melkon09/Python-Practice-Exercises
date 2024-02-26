import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username=="admin" and password=="1234":
        login_status.config(text="Login Successful", fg="green")
    else:
        login_status.config(text="Invalid username and/or password", fg="red")

parent=tk.Tk()
parent.title("Login Form")

username_label = tk.Label(parent, text="Username:")
username_entry = tk.Entry(parent)

password_label = tk.Label(parent, text="Password: ")
password_entry = tk.Entry(parent, show='*')

login_button=tk.Button(parent, text='Login', command=login)

login_status=tk.Label(parent, text='')

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
username_entry.focus()

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, columnspan=2)

login_status.grid(row=3, columnspan=2)

login_button.bind

for child in parent.winfo_children():
    child.grid_configure(padx=10, pady=5)

parent.mainloop()



