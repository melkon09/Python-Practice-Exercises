import tkinter as tk

parent=tk.Tk()
parent.title("Chat Application")

message_history=tk.Text(parent, 
wrap='word', width=40, height=10, state='disabled', )
message