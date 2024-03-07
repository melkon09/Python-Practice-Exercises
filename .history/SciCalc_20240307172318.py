import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("700x500")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=5, pady=5, sticky="NEW")
display.grid_configure(columnspan=5)

tags_func=[ 'rad','deg','M+'       ,'MR'       ,'MC' ,
            'x^y', 'PH','sin'      ,'cos'      ,'tan',
            'log','ln' ,'arc\nsin' ,'arc\ncos' ,'arc\ntan',
            '1/x','n!' ,'sinh'     ,'cosh'     ,'tanh',   
            'n√x','2√x','arc\nsinh','arc\ncosh','arc\ntanh'
               ]

tags_simple=['7', '8', '9', 'C', 'AC',
             '4', '5', '6', 'x', '÷',
             '1', '2', '3', '+', '-',
             '0', ',', '+/-', '='
]

i=0
button_list=[]
for ro in range(0,6):
    for col in range(0,5):
        if tags_func[i]=='M+' or tags_func[i]=='MC' or tags_func[i]=='MR':
            button_list.append(tk.Button(frame, width=2, height=1, bg='grey', fg='red', font=('Helvetica', 10, 'bold'), bd=4, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col)    
        else:
            button_list.append(tk.Button(frame, width=2, height=1, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=4, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col)
        i+=1

i=0
for ro in range(6,10):
    for col in range(0,5):
        if tags_simple[i]=='C' or tags_simple[i]=='AC':
            button_list.append(tk.Button(frame, width=2, height=1, bg='red', fg='white', font=('Helvetica', 10, 'bold'), bd=4, text=tags_simple[i]))
            button_list[i].grid(row=ro, column=col)
        elif tags_simple[i]=='=':
            button_list.append(tk.Button(frame, width=2, height=1, bg='red', fg='white', font=('Helvetica', 10, 'bold'), bd=4, text=tags_simple[i]))
            button_list[i].grid(row=ro, column=col, columnspan=2)
            break
        else:
            button_list.append(tk.Button(frame, width=2, height=1, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=4, text=tags_simple[i]))
            button_list[i].grid(row=ro, column=col)
        i+=1


root.mainloop()