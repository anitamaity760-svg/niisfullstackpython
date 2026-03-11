class ShoppingCart:
    
    # Constructor
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []   # list to store items
        self.total = 0
    
    # Add Item
    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        self.total += price
        print(item_name, "added to cart.")
    
    # Remove Item
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                self.total -= item[1]
                print(item_name, "removed from cart.")
                return
        print("Item not found.")
    
    # Show Cart
    def show_cart(self):
        print("\nItems in Cart:")
        for item in self.items:
            print(item[0], "=", item[1])
        print("Total Amount =", self.total)


# Creating Object
cart1 = ShoppingCart("Rahul")

cart1.add_item("Laptop", 50000)
cart1.add_item("Mouse", 500)
cart1.add_item("Keyboard", 1000)

cart1.remove_item("Mouse")

cart1.show_cart()