import tkinter as tk

parent=tk.Tk()
parent.title("Frame with Place geometry Manager")

frame=tk.Frame(parent, padx=20, pady=20)
frame.pack()

label=tk.Label(frame, text="Name:")
