class ShoppingCart:
    def __init__(self):
        self.cart = {}  # Initialize an empty cart
        self.product_prices = {'123': 10.0, '456': 20.0}  # Example prices

    def add_to_cart(self, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
    
    def update_quantity(self, product_id, new_quantity):
        if product_id in self.cart:
            self.cart[product_id] = new_quantity
        else:
            print(f"Product {product_id} not found in cart.")
    
    def calculate_total_price(self):
        total_price = 0.0
        for product_id, quantity in self.cart.items():
            if product_id in self.product_prices:
                total_price += self.product_prices[product_id] * quantity
            else:
                print(f"Price not found for product {product_id}.")
        return total_price
    
if __name__ == "__main__":
    cart = ShoppingCart()

    # Example usage
    cart.add_to_cart('123', 2)
    cart.add_to_cart('456', 1)
    cart.update_quantity('123', 3)

    total_price = cart.calculate_total_price()
    print(f"Total price: ${total_price:.2f}")