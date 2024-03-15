from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("empty name")
        self.__name = value

    @staticmethod
    @abstractmethod
    def sensors_amount():
        ...


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


# r = Robot()
# print(r)
m = MedicalRobot("Med-Robo")
print(m.name)
print(m.sensors_amount())