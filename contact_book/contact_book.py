contacts = []  

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        new_contact = {"name": name, "phone": phone, "email": email}
        contacts.append(new_contact)
        print(f"{name} added successfully")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            for contact in contacts:
                print(contact["name"], "-", contact["phone"], "-", contact["email"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("Found:", contact["name"], "-", contact["phone"], "-", contact["email"])
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == "4":
        del_name = input("Enter name to delete: ")
        for contact in contacts:
            if contact["name"].lower() == del_name.lower():
                contacts.remove(contact)
                print(f"{del_name} deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
        print(type(contacts))