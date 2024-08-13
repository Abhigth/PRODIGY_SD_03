import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact for {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")

    if name in contacts:
        phone = input(f"Enter new phone number for {name} (or press Enter to keep current): ")
        email = input(f"Enter new email address for {name} (or press Enter to keep current): ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        print(f"Contact for {name} updated.")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.")
    else:
        print(f"No contact found with the name {name}.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit a Contact")
        print("4. Delete a Contact")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()