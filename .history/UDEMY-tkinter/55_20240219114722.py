import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


root= tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('Widget Examples')

text = tk.Text(root, height=8) #height in lines
text.pack()

text.insert("1.0", "Please enter a comment...")  # 1.0: first line, zero character
text["state"]='normal' # 'disabled'

text_content
root.mainloop()

