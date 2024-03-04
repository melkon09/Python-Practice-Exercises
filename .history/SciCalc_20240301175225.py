import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("600x400")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=10, pady=5, sticky="NEW")

tags={'n√x', '1/x', 'rad', 'deg', 'MC', 'MR', 'sin', 'arcsin',
    '2√x', '(', ')', 'n!', '÷', 'M+', 'cos', 'arccos',
    'x^y', '7', '8', '9', 'x', 'ph', 'tan', 'arctan',
    'ph', '4', '5', '6', '-', 'ph', 'sinh', 'arcsinh',
    'log', '1', '2', '3', '+', 'C', 'cosh', 'arccosh',
    'ln', '+/-', '0', ',', '=', 'AC', 'tanh', 'arctanh'    
}

i=0
button_list[]
for col in range(1,6):
    for row



root.mainloop()