#Kenny Tran
#02/27/23
#contact.py function file

contacts = {}

def add_contacts(contacts, /, *, id, first_name, last_name):
    '''This function prompts the user with three messages,
       the phone number, the first name, and the last name.
       After user input, this funtion will add all three
       to a dictionary: contacts'''
    if id in contacts:
        print("\nERROR: Phone number already exists")
        return contacts
    else:
        contacts[id] = ([last_name, first_name, id])
    return contacts

def modify_contacts(contacts, *, first_name, last_name):
    '''This function prompts the user to enter in an ID already
       in the contacts dictionary. This will prompt the user to enter
       a new first name and last name to edit the existing object.'''
    id=input("Enter existing phone number: ")
    if id not in contacts:
        print("\nERROR: Phone number does not exist")
        return contacts
    else:
        first_name=input("Enter new first name: ")
        last_name=input("Enter new last name: ")
        contacts[id][1] = first_name
        contacts[id][0] = last_name
    return contacts

def delete_contacts(contacts, id):
    '''This function prompts the user to enter in an existing ID
       in the dictionary. Upon user input, this will delete the corresponding
       contact to the ID the user entered.'''
    id=input("Enter existing phone number to delete: ")
    if id not in contacts:
        print("\nERROR: Phone number does not exist")
        return contacts
    else:
        deleted_contacts = contacts.pop(id)
        return deleted_contacts
        
def print_contacts(contacts):
    '''This function will print out all the contacts the user has added
       beginning with the last name, first name, then phone number.'''
    print("\n==================== CONTACT LIST ====================\n"
          "Last Name             First Name            Phone\n"
          "====================  ====================  ==========") 
    for contact in contacts.values():
        print(f'{contact[0]:22}{contact[1]:22}{contact[2]:13}')

def sort_contacts(contacts):
    '''This function will display an alphabetically sorted contact list.
       The surname will be sorted first, then the first name.'''
    print("\n==================== CONTACT LIST ====================\n"
          "Last Name             First Name            Phone\n"
          "====================  ====================  ==========")       
    sorted_contacts = sorted(contacts.keys(), key=lambda key: contacts[key][0])
    for key in sorted_contacts:
        value = contacts[key]
        print(f'{value[0]:22}{value[1]:22}{key:13}')
    return contacts

def find_contacts(contacts, find):
    '''This function will prompt the user to enter in a common string
       in order to search for a specific contact. Upon user input, a sorted
       contact list will display every contact with that common string.'''
    search = {}
    for k, v in contacts.items():
        if find in v[0] or find in v[1] or k == find:
            search[k] = v
            
    sort_contacts(search)
    
