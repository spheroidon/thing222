import os
import json
import string

animals = []
SAVE_FILE = "zoo.json"

if os.path.isfile(SAVE_FILE):
    with open(SAVE_FILE, 'r') as file:
        animals = json.load(file)

def main():
    exited = False

    while not exited:
        menuprint()
        action = input("Action: ")
        if action.lower() == "q":
            exited = True
        elif action.lower() == "a":
            addanimal()
            print("Added!")
        elif action.lower() == "e":
            editanimal()
            print("Edited!")
        elif action.lower() == "r":
            removeanimal()
            print("Removed!")
        elif action.lower() == "p":
            printanimals()

    with open(SAVE_FILE, 'w') as file:
        json.dump(animals,file)

def menuprint():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("a - add animal")
        print("r - remove animal")
        print("e - edit animal")
        print("p - print all animals")
        print("q - exit")

def addanimal():
    animal_name = input("Name: ")
    animal_species = input("Species: ")
    animal_age = input("Age: ")
    animals.append({"name": animal_name, "species": animal_species, "age": animal_age})

def editanimal():
    animal_index = int(input("Index: ").strip(string.ascii_letters))
    addanimal()
    if(len(animals) >= animal_index):
        animals.pop(animal_index)

def removeanimal():
    animal_index = input("Index: ")
    print(animals)
    animals.pop(animal_index)

def printanimals():
    i = 0
    for obj in animals:
        print("----------------")
        print(f"Index: {str(i)}")
        print(f"Name: {obj['name']}")
        print(f"Species: {obj['species']}")
        print(f"Age: {obj['age']}")
        i += 1
    input()

if __name__ == "__main__":
    main()