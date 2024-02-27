import tkinter as tk

def add_contact():
    name=name_entry.get()
    if name:
        contacts_listbox.insert('end', name)
        name_entry.delete(0,'end')

def delete_contact():
    selected_index=contacts_listbox.curselection()
    if selected_index:
        contacts_listbox.delete(selected_index)

parent=tk.Tk()
parent.title("Employee List Application")

contacts_listbox=tk.Listbox(parent, selectmode=tk.SINGLE)
contacts_listbox.pack(padx=10, pady=10, fill="both", expand=True)

name_entry=tk.Entry(parent)
name_entry.pack(pady=5)

add_button=tk.Button(parent, text="Add", command=add_contact)
add_button.pack(side='left', padx=5)
delete_button=tk.Button(parent, text='Delete', command=delete_contact)
delete_button.pack(side='left', padx=5)

parent.mainloop()