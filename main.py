from function import *

def menu():
    print('''
---Choose option---:
1. Add contact
2. Show all contacts
3. Search contact
4. Delete contact
5. Edit contact
6. Exit''')

def main():
    running = True
    contacts = load_contacts()
    while running:
        menu()
        print('---Choose an option from 1 to 6---')
        choice = int(input('Enter number'))

        match choice:
            case 1:
                add_contact(contacts)
            case 2:
                all_contact(contacts)
            case 3:
                search_by_name(contacts)
            case 4:
                delete_contact(contacts)
            case 5:
                edit_contact(contacts)
            case 6:
                print('Exit')
                running = False
            case _:
                print('not a option')

main()