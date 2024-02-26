import tkinter as tk

def close_window():
    parent.destroy()

parent=tk.Tk()
parent.title("Close window example")


label=tk.Label(parent, text="Click the 'Close' button to close this window")
label.pack(padx=10, pady=10)

close_button=tk.Button(parent, text="Close Window", command=close_window)
close_button.pack()

parent.mainloop()

