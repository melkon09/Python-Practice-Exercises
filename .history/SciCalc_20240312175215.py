import tkinter as tk
from tkinter import ttk
import math

def square_root():
    result = math.sqrt(float(display.get()))
    display.delete(0, 'end')
    display.insert(0,result)

def num_1():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'1')
    else:
        display.insert(0,'1')    

def num_2():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'2')
    else:
        display.insert(0,'2')

def num_3():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'3')
    else:
        display.insert(0,'3')

def num_4():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'4')
    else:
        display.insert(0,'4')

def num_5():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'5')
    else:
        display.insert(0,'5')

def num_6():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'6')
    else:
        display.insert(0,'6')

def num_7():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'7')
    else:
        display.insert(0,'7')

def num_8():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'8')
    else:
        display.insert(0,'8')

def num_9():
    if display.get()=='0':
        display.delete(0, 'end')
        display.insert(0,'9')
    else:
        display.insert(0,'9')

def num_0():
    if display.get()=='0':
        pass
    else:
        display.insert(0,'1')





















root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("330x620")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=5, pady=5, sticky="NEW")
display.grid_configure(columnspan=5)
display.insert(0, "0")



tags_func=[ 'rad','deg','M+'       ,'MR'       ,'MC' ,
            'x^y', 'e','sin'      ,'cos'      ,'tan',
            'log','ln' ,'arc\nsin' ,'arc\ncos' ,'arc\ntan',
            '1/x','n!' ,'sinh'     ,'cosh'     ,'tanh',    
            'n√x','2√x','arc\nsinh','arc\ncosh','arc\ntanh'
               ]

functions_1=['', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', square_root, '', '', ''
]

tags_simple=['7', '8', '9', 'C', 'AC',
             '4', '5', '6', 'x', '÷',
             '1', '2', '3', '+', '-',
             '0', ',', '+/-', '='
]

functions_2=[ num_7, num_8, num_9, '', 'all_clear',
             num_1, num_2, num_3, '', '',
            num_1, num_2, num_3, '', '',
            num_0, '', '', '', '',]

i=0
button_list=[]
for ro in range(1,6):
    for col in range(0,5):
        if tags_func[i]=='M+' or tags_func[i]=='MC' or tags_func[i]=='MR':
            button_list.append(tk.Button(frame, width=4, height=2, bg='grey', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col, pady=5)    
        else:
            button_list.append(tk.Button(frame, width=4, height=2, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i], command=functions_1[i]))
            button_list[i].grid(row=ro, column=col, pady=5)
        i+=1

i=0
for ro in range(6,10):
    for col in range(0,5):
        if tags_simple[i]=='C' or tags_simple[i]=='AC':
            button_list.append(tk.Button(frame, width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, pady=5)
        elif tags_simple[i]=='=':
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightblue', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, columnspan=2, pady=5, sticky="EW")
            break
        else:
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightgrey', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, pady=5)
        i+=1




root.mainloop()