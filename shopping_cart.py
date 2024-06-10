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