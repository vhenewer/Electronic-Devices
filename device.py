class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def __str__(self):
        return f"{self.name} - {self.price} USD, {self.stock} pieces in stock, Warranty: {self.warranty} months"

    def apply_discount(self, discount_percentage):
        self.price -= self.price * discount_percentage / 100

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        self.stock -= amount
