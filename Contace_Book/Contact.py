contacts = {}

while True:
    print("\n1.Add Contact\n2.View Contacts\n3.Search Contact\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name:- ")
        phone = input("Enter phone number:- ")
        contacts[name] = phone
        print("Contact Saved!")

    elif choice == 2:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 3:
        name = input("Search name:- ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 4:
        break
    else:
        print("Invalid choice!")
