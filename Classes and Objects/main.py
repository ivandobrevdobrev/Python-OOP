class Vehicle:

    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

    def __str__(self):
        return f"This is my car with mileage {self.mileage} and speed {self.max_speed}"
    def __repr__(self):
        return f"This is my car with mileage {self.mileage} and speed {self.max_speed}"


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
car = Vehicle(20,200)

print(car)