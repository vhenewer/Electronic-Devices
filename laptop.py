from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"Laptop: {self.name}, {self.price} USD, {self.stock} in stock, {self.ram_size} GB RAM, {self.processor_speed} GHz processor"

    def run_program(self):
        print(f"Running program on {self.name}...")

    def use_keyboard(self):
        print(f"Typing on {self.name} keyboard...")
