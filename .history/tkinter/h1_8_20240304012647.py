import tkinter as tk
import calendar

def update_calendar():
    cal_text.config(text=calendar.month(year, month))

root=tk.Tk()
root.title('Callendar App')

current_year=2000
