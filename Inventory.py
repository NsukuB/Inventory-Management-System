

class Product:
    def __init__(self, product_id, name, quantity, reorder_level):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.reorder_level = reorder_level

    def __repr__(self):
        return f"{self.name} (ID: {self.product_id}, Quantity: {self.quantity}, Reorder Level: {self.reorder_level})"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product ID {product.product_id} already exists. Updating the quantity.")
            self.products[product.product_id].quantity += product.quantity
        else:
            self.products[product.product_id] = product

    def remove_product(self, product_id, quantity):
        if product_id in self.products:
            if self.products[product_id].quantity >= quantity:
                self.products[product_id].quantity -= quantity
                print(f"Removed {quantity} of {self.products[product_id].name}.")
                if self.products[product_id].quantity == 0:
                    del self.products[product_id]
            else:
                print(f"Insufficient quantity to remove. Only {self.products[product_id].quantity} available.")
        else:
            print("Product ID not found.")

    def check_reorder(self):
        reorder_list = []
        for product_id, product in self.products.items():
            if product.quantity <= product.reorder_level:
                reorder_list.append(product)
        return reorder_list

    def display_inventory(self):
        if self.products:
            for product in self.products.values():
                print(product)
        else:
            print("Inventory is empty.")


# Example usage
inventory = Inventory()

# Adding products to the inventory
inventory.add_product(Product(1, "Laptop", 10, 5))
inventory.add_product(Product(2, "Mouse", 50, 20))
inventory.add_product(Product(3, "Keyboard", 20, 10))

# Displaying the current inventory
print("\nCurrent Inventory:")
inventory.display_inventory()

# Removing some products
inventory.remove_product(1, 3)

# Checking for products that need to be reordered
print("\nProducts that need to be reordered:")
reorder_list = inventory.check_reorder()
for product in reorder_list:
    print(product)

# Displaying the updated inventory
print("\nUpdated Inventory:")
inventory.display_inventory()
