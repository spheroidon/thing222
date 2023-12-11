import os
import json
import string

contacts = []
SAVE_FILE = "contacts.json"

if os.path.isfile(SAVE_FILE):
    with open(SAVE_FILE, 'r') as file:
        contacts = json.load(file)

def main():
    exited = False

    while not exited:
        menuprint()
        action = input("Action: ")
        if action.lower() == "q":
            exited = True
        elif action.lower() == "a":
            addcontact()
            print("Added!")
        elif action.lower() == "e":
            editcontact()
            print("Edited!")
        elif action.lower() == "r":
            removecontact()
            print("Removed!")
        elif action.lower() == "p":
            printcontacts()

    with open(SAVE_FILE, 'w') as file:
        json.dump(contacts,file)

def menuprint():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("a - add contact")
        print("r - remove contact")
        print("e - edit contact")
        print("p - print all contacts")
        print("q - exit")

def addcontact():
    contact_name = input("Name: ")
    contact_phone = input("Phone: ")
    contact_mail = input("Email: ")
    contacts.append({"name": contact_name, "phone": contact_phone, "email": contact_mail})

def editcontact():
    contact_index = int(input("Index: ").strip(string.ascii_letters))
    addcontact()
    if(len(contacts) >= contact_index):
        contacts.pop(contact_index)

def removecontact():
    contact_index = input("Index: ")
    print(contacts)
    contacts.pop(contact_index)

def printcontacts():
    i = 0
    for obj in contacts:
        print("----------------")
        print(f"Index: {str(i)}")
        print(f"Name: {obj['name']}")
        print(f"Number: {obj['phone']}")
        print(f"Email: {obj['email']}")
        i += 1
    input()

if __name__ == "__main__":
    main()