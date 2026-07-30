class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_latte(self):
        if self.water < 200 or self.coffee < 20 or self.milk < 150:
            return False
        else:
            self.water -= 200
            self.coffee -= 20
            self.milk -= 150
            return True
cm = CoffeeMachine(300, 100, 200)
print(f"Latte made! Remaining - water: {cm.water}, coffee: {cm.coffee}, milk: {cm.milk}") if cm.make_latte() else print("Not enough resources to make a latte.")
print(f"Latte made! Remaining - water: {cm.water}, coffee: {cm.coffee}, milk: {cm.milk}") if cm.make_latte() else print("Not enough resources to make a latte.")