import tkinter as tk

def send_message():
    message=message_entry.get()
    if message:
        message_history.config(state='normal')
        message_history.insert('end', f'You: {message}\n')
        message_history.config(state='disabled')
        message_entry
parent=tk.Tk()
parent.title("Chat Application")

message_history=tk.Text(parent, wrap='word', width=40, height=10)
message_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
message_history.config(state='disabled')

message_entry=tk.Entry(parent, width=30)
message_entry.grid(row=1, column=0, padx=10, pady=10)

send_button=tk.Button(parent, text='Send', command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

parent.mainloop()