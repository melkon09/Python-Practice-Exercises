import tkinter as tk

root = tk.Tk()
root.title('Button Click Event Handling')

label=tk.Label(root, text='Click the button and check the message text')
label.pack()

def on_button_click():
    label.config(text='Button Clicked!')

button = tk.Button(root, text='Click Me!', command = on_button_click)
button.pack()

root.mainloop()