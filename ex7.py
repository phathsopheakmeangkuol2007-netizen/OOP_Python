class Light:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
        print(f"Light is ON")
    def turn_off(self):
        self.is_on = False
        print(f"Ligh is OFF")
    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")

l = Light()
l.turn_on()
l.turn_off()
l.status()