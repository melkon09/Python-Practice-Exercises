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
display.grid_configure(columnspan=8)

tags_funct=['n√x', '1/x', 'rad', 'deg', 'MC', 'MR', 'sin', 'arc\nsin',
            '2√x', '(', ')', 'n!', '÷', 'M+', 'cos', 'arc\ncos',
            'x^y', '7', '8', '9', 'x', 'ph', 'tan', 'arc\ntan',
            'ph', '4', '5', '6', '-', 'ph', 'sinh', 'arc\nsinh',
            'log', '1', '2', '3', '+', 'C', 'cosh', 'arc\ncosh',
            'ln', '+/-', '0', ',', '=', 'AC', 'tanh', 'arc\ntanh'
]

tags_simple=['7', '8', '9', 'C', 'AC',
             '4', '5', '6', '', '',
             '', '', '', '', '',
             '', '', '', '', '',
             '', '', '', '', '',
]

i=0
button_list=[]
for ro in range(1,7):
    for col in range(0,8):
        button_list.append(tk.Button(frame, width=2, height=1, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=4, text=tags[i]))
        button_list[i].grid(row=ro, column=col, pady=3)
        i+=1

root.mainloop()