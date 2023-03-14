#Kenny Tran
#02/27/23
#main.py main file

from contacts import *

contacts = {}

while True:
    print("\nEMPLOYEE CONTACT MENU")
    print("\n1. Add Contact\n2. Modify Contact\n3. Delete Contact\n"
          "4. Print Contacts\n5. Sort Contacts\n6. Find Contact\n"
          "7. Exit Program\n")
    choice = (input("\nEnter your choice: "))
    match choice:
        case '1':
            add_contacts(contacts, id=input("Add phone number: "),
                         first_name=input("Enter first name: "),
                         last_name=input("Enter last name: "))
        case '2':
            modify_contacts(contacts, first_name=0, last_name=0)
        case '3':
            delete_contacts(contacts, id)
        case '4':
            print_contacts(contacts)
        case '5':
            sort_contacts(contacts)
        case '6':
            find_contacts(contacts, find=input("Enter search string: "))
        case '7':
            print("\nEXITING PROGRAM")
            break
        case _:
            print("\nERROR: Please enter a menu option from 1 - 7")
        
            
