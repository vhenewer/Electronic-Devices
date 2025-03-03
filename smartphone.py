from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"Smartphone: {self.name}, {self.price} USD, {self.stock} in stock, {self.screen_size}\" screen, {self.battery_life} hours battery"

    def make_call(self):
        print(f"Making a call on {self.name}...")

    def install_app(self):
        print(f"Installing an app on {self.name}...")
