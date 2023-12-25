import tkinter as tk
from tkinter import messagebox

contacts = [] 


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }

    contacts.append(contact)
    messagebox.showinfo("Success", "Contact added successfully!")


def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"Name: {contact['Name']} - Phone: {contact['Phone']} - Email: {contact['Email']} - Address: {contact['Address']}")


def search_contact():
    search_term = search_entry.get()
    search_result = []

    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            search_result.append(contact)

    contact_list.delete(0, tk.END)
    for contact in search_result:
        contact_list.insert(tk.END, f"Name: {contact['Name']} - Phone: {contact['Phone']} - Email: {contact['Email']} - Address: {contact['Address']}")


def update_contact():
    selected_index = contact_list.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a contact to update.")
        return

    selected_contact = contacts[selected_index[0]]

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    selected_contact['Name'] = name
    selected_contact['Phone'] = phone
    selected_contact['Email'] = email
    selected_contact['Address'] = address

    messagebox.showinfo("Success", "Contact updated successfully!")


def delete_contact():
    selected_index = contact_list.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return

    contacts.pop(selected_index[0])
    messagebox.showinfo("Success", "Contact deleted successfully!")


root = tk.Tk()
root.title("Contact Manager")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky='w')
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky='w')
tk.Label(root, text="Email:").grid(row=2, column=0, sticky='w')
tk.Label(root, text="Address:").grid(row=3, column=0, sticky='w')

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=5)
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=0, columnspan=2, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=0, pady=5)
search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=6, column=1, pady=5)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=7, column=0, columnspan=2, pady=5)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, column=0, columnspan=2, pady=5)

contact_list = tk.Listbox(root, width=70)
contact_list.grid(row=0, column=2, rowspan=9, padx=10)

root.mainloop()
