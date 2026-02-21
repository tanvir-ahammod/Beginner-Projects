import json

FILENAME = "contacts.json"

def load_contacts():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4) 

contacts=load_contacts()

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice=input("Choose an option (1-5): ")

    if choice=="1":
        name=input("Enter contact name: ")
        phone=input("Enter contact phone number: ")
        contacts[name]=phone
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully!")

    elif choice=="2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nYour Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice=="3":
        search_name=input("Enter the name to search: ")
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print(f"Contact '{search_name}' not found.")

    elif choice=="4":
        delete_name=input("Enter the name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            save_contacts(contacts)
            print(f"Contact '{delete_name}' deleted successfully!")
        else:
            print(f"Contact '{delete_name}' not found.")

    elif choice=="5":
        print("Exiting the Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 5.")