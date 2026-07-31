class Media:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def describe(self):
        pass
    
class Book(Media):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author
    def describe(self):
        print(f"{type(self).__name__}: {self.name} by {self.author} - Rs.{self.price}")

class Magazine(Media):
    def __init__(self, name, price, frequency):
        super().__init__(name, price)
        self.frequency = frequency
    def describe(self):
        print(f"{type(self).__name__}: {self.name} ({self.frequency}) - Rs.{self.price}")

class DVD(Media):
    def __init__(self, name, price, duration):
        super().__init__(name, price)
        self.duration = duration
    def describe(self):
        print(f"{type(self).__name__}: {self.name}, {self.duration} mins - Rs.{self.price}")

items = [
    Book("Clean Code", 499, "Robert C. Martin"), 
    Magazine("Wired", 150, "Monthly"), 
    DVD("Inception", 299, 148)
]

for item in items:
    item.describe()
