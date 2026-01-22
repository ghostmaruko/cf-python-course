class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} added to the list.")
        else:
            print(f"{item} is already in the list.")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    def view_list(self):
        print(f"\n{self.list_name}:")
        for item in self.shopping_list:
            print(f"- {item}")


# Create the shopping list object
pet_store_list = ShoppingList("Pet Store Shopping List")

# Add items
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

# Remove an item
pet_store_list.remove_item("flea collars")

# Try adding a duplicate item
pet_store_list.add_item("frisbee")

# View the final shopping list
pet_store_list.view_list()
