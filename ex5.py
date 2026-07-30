class Product:
    def __init__(self, name, price, quatity):
        self.name = name
        self.price = price
        self.quatity = quatity
    def total_value(self):
        return self.price * self.quatity
p1 = Product("Laptop", 899.99, 5)
print(f"Total stock value of {p1.name}: ${p1.total_value()}")