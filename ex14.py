class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def seating_capacity(self, capacity):
        print(f"{self.name} have seating capacity: {capacity}")
class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)
bus = Bus("School Bus", 120)
bus.seating_capacity()
