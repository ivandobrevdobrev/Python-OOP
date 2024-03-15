from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_Conditioner: float = 0.9

    def drive(self, distance):
        consumption = (self.AIR_Conditioner + self.fuel_consumption) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    AIR_Conditioner: float = 1.6
    TANK_PERCENTAGE_FILL: float = 0.95

    def drive(self, distance):
        consumption = (self.AIR_Conditioner + self.fuel_consumption) * distance
        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.TANK_PERCENTAGE_FILL


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
