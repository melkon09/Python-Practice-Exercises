import tkinter as tk

parent=tk.Tk()
parent.title=("Customizing Labels and Buttons")
parent.geometry("400x400")

label=tk.Label(parent, text="Custom Label", font=("Arial", 18), fg='white', bg='red')
label.pack(pady=10)

button=tk.Button(parent, text='Custom Button', font=('Helvetica', 14), fg='white', bg='blue', activebackground='red', activeforeground="white", )
button.pack(pady=10)

parent.mainloop()