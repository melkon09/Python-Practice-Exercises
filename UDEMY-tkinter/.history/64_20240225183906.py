import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root=tk.Tk()
root.title("Distance converter")

main =ttk.Frame(root, padding=(30, 50))
main.grid()

meters_label=ttk.Label(main, text="Meters:")
meters_input=ttk.Entry(main, width=10)
feet_label=ttk.Label(main, text="Feet")



root.mainloop()