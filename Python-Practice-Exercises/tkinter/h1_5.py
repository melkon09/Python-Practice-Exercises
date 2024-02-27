import tkinter as tk

# Create the main Tkinter window
parent = tk.Tk()
parent.title("Frame with Place Geometry Manager")

# Create a Frame widget
frame = tk.Frame(parent, padx=20, pady=20)
frame.pack()

# Create labels, Entry widgets, and buttons
label1 = tk.Label(frame, text="Name:")
entry1 = tk.Entry(frame)
label2 = tk.Label(frame, text="Email:")
entry2 = tk.Entry(frame)
button1 = tk.Button(frame, text="Submit")
button2 = tk.Button(frame, text="Clear")

# Place widgets inside the Frame using the Place geometry manager
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack()
button2.pack()

# Run the Tkinter main loop
parent.mainloop()
