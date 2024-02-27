import tkinter as tk

parent=tk.Tk()
parent.title("Frame with Place geometry Manager")

frame=tk.Frame(parent, padx=20, pady=20)
frame.pack()

label1=tk.Label(frame, text="Name:")
entry1=tk.Entry(frame)
label2=tk.Label(frame, text="Email:")
entry2=tk.Entry(frame)
button1=tk.Button(frame, text="Submit")
button2=tk.Button(frame, text='Clear')

label1.pack()
label2.pack()
entry1.pack()
enry