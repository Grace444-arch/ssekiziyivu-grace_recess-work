inventory = {
    "T-shirts": 50,
    "Hoodies": 30,
    "Jeans": 20,
    "Sneakers": 15
}

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print("\n")

def update_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Updated {item} quantity to {inventory[item]}")

def remove_item(item):
    if item in inventory:
        del inventory[item]
        print(f"Removed {item} from inventory")
    else:
        print(f"{item} not found in inventory")

# Main loop
while True:
    print("1. Display Inventory")
    print("2. Update Inventory")
    print("3. Remove Item")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_inventory()
    elif choice == "2":
        item = input("Enter item name to update: ")
        try:
            quantity = int(input("Enter quantity to add: "))
            update_inventory(item, quantity)
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    elif choice == "3":
        item = input("Enter item name to remove: ")
        remove_item(item)
    elif choice == "4":
        print("Exiting inventory management system.")
        break
    else:
        print("Invalid choice, please try again.")
