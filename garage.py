import os
import json
import string

cars = []
SAVE_FILE = "garage.json"

if os.path.isfile(SAVE_FILE):
    with open(SAVE_FILE, 'r') as file:
        cars = json.load(file)

def main():
    exited = False

    while not exited:
        menuprint()
        action = input("Action: ")
        if action.lower() == "q":
            exited = True
        elif action.lower() == "a":
            addcar()
            print("Added!")
        elif action.lower() == "e":
            editcar()
            print("Edited!")
        elif action.lower() == "r":
            removecar()
            print("Removed!")
        elif action.lower() == "p":
            printcars()

    with open(SAVE_FILE, 'w') as file:
        json.dump(cars,file)

def menuprint():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("a - add car")
        print("r - remove car")
        print("e - edit car")
        print("p - print all cars")
        print("q - exit")

def addcar():
    car_color = input("Color: ")
    car_brand = input("Brand: ")
    car_model = input("Model: ")
    cars.append({"color": car_color, "brand": car_brand, "model": car_model})

def editcar():
    car_index = int(input("Index: ").strip(string.ascii_letters))
    addcar()
    if(len(cars) >= car_index):
        cars.pop(car_index)

def removecar():
    car_index = input("Index: ")
    print(cars)
    cars.pop(car_index)

def printcars():
    i = 0
    for obj in cars:
        print("----------------")
        print(f"Index: {str(i)}")
        print(f"Color: {obj['color']}")
        print(f"Number: {obj['brand']}")
        print(f"Model: {obj['model']}")
        i += 1
    input()

if __name__ == "__main__":
    main()