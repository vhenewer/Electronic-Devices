class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            print(f"Added {amount} of {device.name} to the cart.")
        else:
            print(f"Not enough stock for {device.name}. Only {device.stock} left.")

    def remove_device(self, device, amount):
        for i, (item, item_amount) in enumerate(self.items):
            if item == device:
                if item_amount >= amount:
                    item_amount -= amount
                    self.total_price -= item.price * amount
                    device.stock += amount
                    self.items[i] = (item, item_amount)
                    print(f"Removed {amount} of {device.name} from the cart.")
                    break
                else:
                    print(f"Cannot remove more than {item_amount} of {device.name} from the cart.")
                    break
        else:
            print(f"{device.name} is not in the cart.")

    def change_quantity(self, device, new_amount):
        for i, (item, item_amount) in enumerate(self.items):
            if item == device:
                old_amount = item_amount
                item_amount = new_amount
                self.total_price -= item.price * old_amount
                self.total_price += item.price * item_amount
                self.items[i] = (item, item_amount)
                print(f"Changed quantity of {device.name} to {new_amount} in the cart.")
                break
        else:
            print(f"{device.name} is not in the cart.")

    def apply_discount(self, discount_percentage):
        discount = self.total_price * discount_percentage / 100
        self.total_price -= discount
        print(f"Applied {discount_percentage}% discount. New total price: {self.total_price} USD.")

    def clear_cart(self):
        self.items.clear()
        self.total_price = 0.0
        print("Cart has been cleared.")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for item, amount in self.items:
            print(f"{item.name} - {amount} pieces")

    def checkout(self):
        print("Checkout summary:")
        for item, amount in self.items:
            print(f"{item.name}: {amount} pieces")
        print(f"Total price: {self.total_price} USD")
        print("Thank you for shopping!")
