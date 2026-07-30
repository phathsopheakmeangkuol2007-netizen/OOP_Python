class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed}")
class Bus(Vehicle):
    pass
bus1 = Bus("School Bus", 120)
bus1.display()