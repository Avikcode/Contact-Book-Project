import json


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        return contacts
    except Exception as e:
        print(e)
        return []

def dump_contacts(contacts):
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print(e)

def add_contact(contacts):
    name = input("Enter a name: ")
    number = input("Enter number: ")
    if search(contacts, {"name": name, "number": number}):
        print("have ...")
        return None
    contacts.append({"name":name, "number":number})
    dump_contacts(contacts)
    print("Added!")

def delete_contact(contacts):
    name = input("Enter a name: ")
    number = input("Enter number: ")
    if not search(contacts, {"name":name, "number":number}):
        print( "Error!!! not found")
        return
    contacts.remove({"name": name, "number": number})
    dump_contacts(contacts)
    print("deleted!")

def search(contacts, contact):
    return contact in contacts


def search_by_name(contacts):
    name = input('Enter a name')
    for n in contacts:
        if n['name'] == name:
            print('name found')
            return
    print('not found')


def all_contacts(contacts):
    print(f'all_contacts: {contacts}')


def edit_contact(contacts):
    name = input('Enter a name')
    number = input('Enter number')

    for contact in contacts:
        if name == contact['name'] and number == contact['number']:
            print('you can edit')

            new_name = input('Enter another name')
            new_number = input('Enter another number')
            contact['name'] = new_name
            contact['number'] = new_number
            dump_contacts(contacts)
            print('contact saved')
            return
    print('not found , can"t edit!')

