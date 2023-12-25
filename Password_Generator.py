import random
import string
import tkinter as tk
import pyperclip

root = tk.Tk()

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(length_entry.get())))
    password_label.config(text=password)

def copy_password():
    pyperclip.copy(password_label['text'])  

instruction_label = tk.Label(root, text="Enter length:")
instruction_label.grid(row=0, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=0, column=2)

copy_button = tk.Button(root, text="Copy", command=copy_password) 
copy_button.grid(row=0, column=3)

password_label = tk.Label(root, text="") 
password_label.grid(row=1, column=0, columnspan=4)

root.title("Random Password Generator")  
root.mainloop()
