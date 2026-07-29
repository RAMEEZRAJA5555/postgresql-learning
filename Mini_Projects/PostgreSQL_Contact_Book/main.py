from database import engine
from models import Base
                                #import all the function which are available in crud.py
from crud import (
    create_contact,
    view_contacts,
    search_contact,
    update_contact,
    delete_contact
)

Base.metadata.create_all(bind=engine)
                                  #that while loop will run forever untill break
while True:

    print("1. Create Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_contact()

    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")