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
display.grid_configure(columnspan=5)

tags=[, , , , , , ,
      , , , , , , ,
      , , ,
      , ,
     , , ,
      , , 
]

tags_func=[ 'rad','deg','M+'       ,'MR' ,'MC' ,
            'x^y',     ,'sin'      ,'cos','tan',
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
for ro in range(1,7):
    for col in range(0,5):
        button_list.append(tk.Button(frame, width=2, height=1, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=4, text=tags[i]))
        button_list[i].grid(row=ro, column=col, pady=3)
        i+=1

root.mainloop()