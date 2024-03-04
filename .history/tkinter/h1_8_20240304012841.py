import tkinter as tk
import calendar

def update_calendar():
    cal_text.config(text=calendar.month(year, month))

root=tk.Tk()
root.title('Callendar App')

current_year=2000
current_month=2
cal_text=tk.Label(root, text='')
cal_text.grid(row=0, column=1, columnspan=7, padx=11, pady=11)
update_calendar(current_year, current_month)

def prev_month():
    global