from database import SessionLocal
from models import Contact  

                                    #create function to create contact
def create_contact():

    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

                                           #Create Session
    session = SessionLocal()

                                      #Create Contact Object
    new_contact = Contact(
        name=name,
        phone=phone,
        email=email
    )

                                     #Add new contact in session
    session.add(new_contact)

                                           #Save changes
    session.commit()

                                     #Close the database session
    session.close()
                         

                        #create view contact function to view all contacts
                        #this function reads all contacts not one contacts
def view_contacts():

    session = SessionLocal()

    contacts = session.query(Contact).all()

    if contacts:
        for row in contacts:
            print(f"ID: {row.id}")
            print(f"Name: {row.name}")
            print(f"Phone: {row.phone}")
            print(f"Email: {row.email}")
    else:
        print("No contacts found.")

    session.close()


def search_contact():

    session=SessionLocal()
                        # we will search contact either any column name,(e.g:id,name,phone,email)
    name=input("enter name to search contact:")
                           
    search_contact=session.query(Contact).filter_by(name=name).first()

    if search_contact:
        print(f"ID: {search_contact.id}")
        print(f"Name: {search_contact.name}")
        print(f"Phone: {search_contact.phone}")
        print(f"Email: {search_contact.email}")
    else:
        print("Contact not found.")

    session.close()

# create update contact function
def update_contact():

    session = SessionLocal()

    contact_id = int(input("Enter contact ID to update: "))

    contact = session.query(Contact).filter_by(id=contact_id).first()

    if contact:

        contact.name = input("Enter new name: ")
        contact.phone = input("Enter new phone: ")
        contact.email = input("Enter new email: ")

        session.commit()
        print("Contact updated successfully.")

    else:
        print("Contact not found.")

    session.close()

# create delete contact function
def delete_contact():

    session = SessionLocal()

    contact_id = int(input("Enter contact ID to delete: "))

    contact = session.query(Contact).filter_by(id=contact_id).first()

    if contact:

        session.delete(contact)

        session.commit()

        print("Contact deleted successfully.")

    else:
        print("Contact not found.")

    session.close()








