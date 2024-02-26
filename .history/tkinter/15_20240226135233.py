import tkinter as tk

def celsiusToFahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius*9/5) +32
        result_label.config(text=f'{celsius:.2f}°C = {fahrenheit:.2f}°F')
    except ValueError:
        result_label.config(text='Invalid Input')

def fahrenheitToCelsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32)*5/9
        result_label.config(text=f'{fahrenheit:.2f}°F = {celsius:.2f}°C')
    except ValueError:
        result_label.config(text="Invalid Input")
    
parent = tk.Tk()
parent.title("Temperature Converter")

celsius_label = tk.Label(parent, text="Input Celsius: ")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(parent)
celsius_entry.grid(row=0, column=1)

c_to_f_button = tk.Button(parent, text="Convert to Fahrenheit", command=celsiusToFahrenheit)
c_to_f_button.grid(row=0, column=2)

fahrenheit_label = tk.Label(parent, text="Input Fahrenheit: ")
fahrenheit_label.grid(row=1, column=0)

fahrenheit_entry = tk.Entry(parent)
fahrenheit_entry.grid(row=1, column=1)

f_to_c_button = tk.Button(parent, text="Convertto Celsius", command=fahrenheitToCelsius)
f_to_c_button.grid(row=1, column=2)

result_label = tk.Label(parent, text="", font=("Helvetica", 14))
result_label.grid(row=2, columnspan=3)

parent.mainloop()