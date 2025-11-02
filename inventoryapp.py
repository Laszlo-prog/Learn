#create inventory app
class Inventory:
    #Initialize  inventory with empty dictionary
    def __init__(self):
        self.items = { }

    def add_item(self):
        name = input("Enter item name:")
        quantity = int(input("Enter item quantity:"))
        self.items[name] = self.items.get(name, 0) + quantity
        print(f"Added {quantity} of {name}.")

    #Remove item from inventory
    def remove_item(self):
        name = input("Enter item name to remove: ")
        if name in self.items:
            del self.items[name]
            print(f"Removed {name} from inventory.")
        else:
            print("Item not found in inventory.")

    #view intvetory
    def show_invetory(self):
        if not self.items:
            print("Inventory is empty.")
            return
        else:
            for name, quantity in self.items.items():
                print(f"{name}: {quantity}")
     #Serach for an item
    def search_item(self):
        name = input("Enter item name to search: ")
        if name in self.items:
            print(f"{name}: {self.items[name]}")
        else:
            print(f"{name} not found in inventory.")
#Display menu and handle user choices
def menu():
    inventory = Inventory()
    options = {
        '1': inventory.add_item,
        '2': inventory.remove_item,
        '3': inventory.show_invetory,
        '4': inventory.search_item,
        '5': exit}
   
    while True:
        print("\nInventory Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Inventory")
        print("4. Search Item")
        print("5. Exit")
        choice = input("Choose an option: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
   


        
