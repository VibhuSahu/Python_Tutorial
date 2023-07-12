class Item:

    pay_rate = 0.8   # The pay rate after 20% discount
    all = []

    # Constructor
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero "
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero "  # help you to give error

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"The details : {name}, price - {price}, quantity - {quantity}")

        # Actions to executte
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        return self.price





item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)


print(item1.name)
print(item1.calculate_total_price())

print(Item.pay_rate)
print(item1.pay_rate)
print(Item.__dict__)        # All the attributes for class level
print(item1.__dict__)       # All the attributes for instance level

item2.apply_discount()
print(item2.price)