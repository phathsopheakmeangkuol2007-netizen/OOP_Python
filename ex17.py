class Employee:
    def __init__(self, name):
        self.name = name
    def calculate_pay(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, anual_salary):
        super().__init__(name)
        self.anual_salary = anual_salary
        
    def calculate_pay(self):
        return self.anual_salary / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_works):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_works = hours_works
    
    def calculate_pay(self):
        return self.hourly_rate * self.hours_works

ft = FullTimeEmployee("Alice", 60000)
pt = PartTimeEmployee("Bob", 500, 20)

print(f"{ft.name}'s monthly pay: {ft.calculate_pay()}")
print(f"{pt.name}'s monthly pay: {pt.calculate_pay()}")


