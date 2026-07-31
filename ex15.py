class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = self.base_fare * 0.10
    def total_fare(self):
        return self.maintenance_fee + self.base_fare
taxi = Taxi(500)
print(f"Total fare with maintenance fee: {taxi.total_fare()}")
