import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.configure(background="#f0f0f0")

        title_label = tk.Label(root, text="Contact Book", font=("Times New Roman ", 20), bg="#6ca0dc", fg="white", padx=10, pady=5)
        title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:", bg="#f0f0f0")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:", bg="#f0f0f0")
        self.phone_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:", bg="#f0f0f0")
        self.email_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address:", bg="#f0f0f0")
        self.address_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg="#4caf50", fg="white")
        self.add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact, bg="#4caf50", fg="white")
        self.search_button.grid(row=6, column=0, padx=10, pady=5)

        self.view_button = tk.Button(root, text="View All Contacts", command=self.view_contacts, bg="#4caf50", fg="white")
        self.view_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.contact_listbox = tk.Listbox(root, width=50)
        self.contact_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, bg="#4caf50", fg="white")
        self.update_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, bg="#4caf50", fg="white")
        self.delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

        made_by_label = tk.Label(root, text="Made by - Harsh Bhardwaj", bg="#f0f0f0")
        made_by_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter name and phone number.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            self.contact_listbox.delete(0, tk.END)
            for contact in self.contacts:
                if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                    self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
        else:
            messagebox.showwarning("Warning", "Please enter search term.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_contact = self.contacts[index]

            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone:
                selected_contact["Name"] = name
                selected_contact["Phone"] = phone
                selected_contact["Email"] = email
                selected_contact["Address"] = address
                self.clear_entries()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showwarning("Warning", "Please enter name and phone number.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
