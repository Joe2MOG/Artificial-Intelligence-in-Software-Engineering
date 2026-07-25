class InvalidProductDataError(ValueError):
    """Custom exception raised for invalid product attributes."""
    pass


class Product:
    """Represents a product with a name, price, and quantity."""
    def __init__(self, name, price, quantity):
        self.name = name
        # These assignments now route through the property setters below
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """Getter for price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price with validation."""
        if value <= 0:
            raise InvalidProductDataError(f"Price must be greater than zero. Received: {value}")
        self._price = value

    @property
    def quantity(self):
        """Getter for quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Setter for quantity with validation."""
        if value < 0:
            raise InvalidProductDataError(f"Quantity cannot be negative. Received: {value}")
        self._quantity = value


class InventoryManager:
    """Manages the collection of products and provides inventory operations."""
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add_product(self, product):
        """Adds a product object to the inventory list."""
        self.inventory.append(product)

    def update_quantity(self, name, new_quantity):
        """Updates the quantity of a product by name."""
        for product in self.inventory:
            if product.name == name:
                product.quantity = new_quantity
                break

    def calculate_total_value(self):
        """Calculates the total monetary value of all inventory."""
        total = 0
        for product in self.inventory:
            total += product.price * product.quantity
        return total

    def display_inventory(self):
        """Prints the current inventory list."""
        for product in self.inventory:
            print(f"{product.name} - ${product.price:.2f} x {product.quantity}")


# Demo Usage
manager = InventoryManager()

try:
    manager.add_product(Product("Laptop", 1200.00, 5))
    manager.add_product(Product("Mouse", 25.00, 20))
    manager.update_quantity("Mouse", 18)
    print("Attempting to set an invalid quantity...")
    manager.update_quantity("Laptop", -2)
except InvalidProductDataError as e:
    print(f"Validation Error Caught: {e}\n")

print("Current Inventory:")
manager.display_inventory()
print(f"\nTotal Inventory Value: ${manager.calculate_total_value():.2f}")

print("\n--- Testing Invalid Input ---")
try:
    manager.inventory[0].quantity = -5
except Exception as e:
    print(f"Test result: {e}")
