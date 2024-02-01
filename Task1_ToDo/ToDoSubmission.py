import customtkinter as ctk
from CTkListbox import *

root = ctk.CTk()
root.geometry("750x750")
root.title("ToDo APP for #CodSoft by Vamsi Devarapalli")

# Funcs
def add_todo():
    current_todo = Text_Field.get()
    lb_tasks.insert(lb_tasks.size(), current_todo)
    Text_Field.delete(0, ctk.END)

def del_todo():
    current_todo = lb_tasks.curselection()
    lb_tasks.delete(current_todo)

def clear_listbox():
    lb_tasks.delete('all')

title_label = ctk.CTkLabel(root, text="Tasks' List", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=20, pady=(40, 20))

sub_title_label = ctk.CTkLabel(root, text='"Today\'s TO-DOs are Tomorrow\'s Triumph"', font=ctk.CTkFont(size=20, weight="bold"))
sub_title_label.pack(padx=10, pady=(0, 20))

lb_tasks = CTkListbox(root, width=500, height=200)
lb_tasks.pack()

Text_Field = ctk.CTkEntry(root, width=500, height=50, placeholder_text="Add todo")
Text_Field.pack(pady=(10, 10))

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=10)

del_button = ctk.CTkButton(root, text="Delete Task", width=500, command=del_todo)
del_button.pack(pady=10)

del_button = ctk.CTkButton(root, text="Delete All", width=500, command=clear_listbox)
del_button.pack()

root.mainloop()
