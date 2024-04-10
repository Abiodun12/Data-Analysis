class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to the cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from the cart.")
        else:
            print(f"{item} is not in the cart.")

    def show_cart(self):
        if self.items:
            print("Items in the cart:")
            for item in self.items:
                print("-", item)
        else:
            print("The cart is empty.")
# Create a cart instance
cart = Cart()

# Add items to the cart
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Orange")

# Show the contents of the cart
cart.show_cart()

# Remove an item from the cart
cart.remove_item("Banana")

# Show the updated contents of the cart
cart.show_cart()
