                   # Polymorphism


# class Shape:
#     def calculate_area(self):
#         return None
#
#
# class Square(Shape):
#     side_length = 2
#
#     def calculate_area(self):
#         return self.side_length * 2
#
#
# class Triangle(Shape):
#     base_length = 4
#     height = 3
#
#     def calculate_area(self):
#         return 0.5 * self.base_length * self.height
#
#
# class Circle(Shape):
#     radius = 3
#
#     def calculate_area(self):
#         return 3.14 * (self.radius ** 2)
#
#
# shapes = [Triangle(), Square(), Circle()]
# for s in shapes:
#     print(s.calculate_area())


               # oveloading operants

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


person_one = Person('John', 20)
person_two = Person('Natasha', 36)
print(person_one > person_two)  # False
