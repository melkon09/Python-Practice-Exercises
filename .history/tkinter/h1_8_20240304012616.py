import tkinter as tk
import calendar

def update_calendar():
    cal_text.config(text=calendar.month(year, month))

    