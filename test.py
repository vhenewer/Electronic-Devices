from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart

iphone = Smartphone("iPhone 13", 999, 50, 12, 6.1, 20)
macbook = Laptop("MacBook Pro", 1999, 30, 24, 16, 3.1)
ipad = Tablet("iPad Pro", 799, 100, 12, "2048x1536", 500)

cart = Cart()

cart.add_device(iphone, 2)
cart.add_device(macbook, 1)
cart.add_device(ipad, 3)

cart.print_items()

cart.apply_discount(10)

cart.change_quantity(iphone, 3)

cart.remove_device(ipad, 1)

cart.checkout()

cart.clear_cart()
