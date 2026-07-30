class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return 1.80 * self.celsius + 32
    def to_kelvin(self):
        return self.celsius + 273.15
t = Temperature(100) 
print(f"Celsius: {t.celsius}")
print(f"Fahrenheit: {t.to_fahrenheit()}")
print(f"Kelvin: {t.to_kelvin()}")
