class Animal:
    def speak(self):
        return "Say something"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Dog(Animal):
    def speak(self):
        return "Woof!"
dog = Dog()
cat = Cat()
print(f"Dog says:", dog.speak())
print(f"Cat says:", cat.speak())
        
