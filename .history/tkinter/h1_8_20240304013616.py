import tkinter as tk
import calendar


def update_calendar(year, month):
    cal_text.config(text=calendar.month(year, month))


root=tk.Tk()
root.title('Calendar App')


current_year=2024
current_month=3
cal_text=tk.Label(root, text='', font=(Consolas, 10))
cal_text.grid(row=0, column=1, columnspan=7, padx=11, pady=11)
update_calendar(current_year, current_month)


def prev_month():
    global current_year, current_month
    current_month -=1
    if current_month<1:
        current_year-=1
        current_month=12
    update_calendar(current_year, current_month)

def next_month():
    global current_year, current_month
    current_month +=1
    if current_month>12:
        current_year+=1
        current_month=1
    update_calendar(current_year, current_month)

prev_button=tk.Button(root, text='Previous', command=prev_month)
prev_button.grid(row=1, column=0, padx=10, pady=10)    

next_button=tk.Button(root, text='Next', command=next_month)
next_button.grid(row=1, column=9, padx=10, pady=10)    

root.mainloop()