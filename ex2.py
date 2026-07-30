class Vehicle:
    def __init__(self, name ,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle name: {vehicle1.name}, Max speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")