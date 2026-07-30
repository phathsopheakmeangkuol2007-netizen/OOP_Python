class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
rect = Rectangle(10, 4)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")