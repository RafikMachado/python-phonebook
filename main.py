from phonebook.phonebook import Phonebook

pb = Phonebook()

def menu():
    print("\n--- Phonebook Manager ---")
    print("1) Add Contact")
    print("2) Delete Contact")
    print("3) Search Contact")
    print("4) View All Contacts")
    print("5) Save Contacts")
    print("0) Exit")

while True:
    menu()
    choice = input("Choose: ").strip()

    if choice == "1":
        first = input("First name: ")
        last  = input("Last name: ")
        phone = input("Phone number: ")
        email = input("Email: ")
        pb.add(first, last, phone, email)

    elif choice == "2":
        phone = input("Enter phone number to delete: ")
        pb.remove(phone)

    elif choice == "3":
        term = input("Search term: ")
        pb.search(term)

    elif choice == "4":
        pb.list_all()

    elif choice == "5":
        pb.save()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
