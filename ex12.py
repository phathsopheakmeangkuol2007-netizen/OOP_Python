class Vehicle:
    color = "White"
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
v1 = Vehicle("Tesla", 250)
v2 = Vehicle("BMW", 200)
print(f"{v1.name} - Color: {v1.color}, Speed: {v1.speed}")
print(f"{v2.name} - Color: {v2.color}, Speed: {v2.speed}")

#changing color
Vehicle.color = "Red"
print(f"{v1.name} - Color: {v1.color}, Speed: {v1.speed}")
print(f"{v2.name} - Color: {v2.color}, Speed: {v2.speed}")
