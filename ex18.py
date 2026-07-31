class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, redius):
        self.redius = redius
    def area(self):
        return 3.14 * self.redius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(7), Square(4), Triangle(6, 8)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")

