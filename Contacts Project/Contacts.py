
contacts = {}  # Dictionary to store contacts


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")


def add_contact():
    name = input("Enter the contact name: ").lower()
    number = input("Enter the contact number: ")
    contacts[name] = number

    print("Contact added successfully.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

2

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    if name in contacts:
        number = input("Enter the new contact number: ")
        contacts[name] = number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\nContact Phone Book")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            print("Thank you for using the Contact Phone Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()