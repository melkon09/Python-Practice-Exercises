import tkinter as tk

parent=tk.Tk()
parent.title("Frame with Place geometry Manager")

frame=tk.Frame(parent, padx=20, pady=20)
frame.pack()

label1=tk.Label(frame, text="Name:")
entry1=tk.Entry(frame)
label2=tk.Label(frame, text="Email:")