import tkinter as tk
parent=tk.Tk()
parent.title('Parent window')

label=tk.Label(parent, text='Click the button and check the label text:')
label.pack()

count = 0
def on_button_click():
    label.config(text='Button clicked!')
    count = count + 1
    if count > 3:
        label.config(text='Το γάμησες και ψόφησε!')

button=tk.Button(parent, text='Click Me!', command = on_button_click)
button.pack()

parent.mainloop()