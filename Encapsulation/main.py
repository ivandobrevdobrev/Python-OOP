# class Person:
#     def __init__(self, name, age=25):
#         self._name = name  # protected
#         self.age = age  # public
#         self.__example = "5"  # private
#
#     def call_example(self):
#         return f"private example is {self.__example} "
#
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def say_hi(self):
#         return f"Hello my name is {self._name}"
#
#     def access_private(self):
#         return f"private is {self.__example}"
#
#
# p = Person("Ivan")
# print(p._name)  # access protected name
# print(p.call_example())  # accessing private through his Class
# print(p._Person__example)
# p._Person__example = "5656"
# print(p._Person__example)
# s = Student("Gosho", 30, "123235")
# print(s.access_private())  # cannot access private attr in inherited class
# print(s.say_hi())
# print(Student.say_hi(s))


# GETTER & SETTER

# class Car:
#     def __init__(self, max_speed: int):
#         self.max_speed = max_speed
#
#     def drive(self):
#         print('driving max speed ' + str(self.max_speed))
#
#     @property
#     def max_speed(self):
#         return self.__max_speed
#
#     @max_speed.setter
#     def max_speed(self, value):
#         if value > 447:
#             value = 447
#         self.__max_speed = value
#
#
# red_car = Car(200)
# red_car.drive()  # driving max speed 200
# red_car.max_speed = 512  # changes the speed to 447
# red_car.drive()


#Built in Attributes

class Person:
    def __init__(self, name):
        self.name = name
        self.money = 40

    # def __getattr__(self, item):
    #     return None

    def __setattr__(self, attr, value):  # всеки атрибут ще се сетне да получава ст-ст 50
        self.__dict__[attr] = 50

    def __delattr__(self, attr):
        del self.__dict__[attr]
        print(f"{attr} was deleted")

#getattr
person = Person('Peter')
# print(getattr(person, 'name'))  # True
# print(getattr(person, 'age'))  # AttributeError
#print(getattr(person, 'age', None))  # None

#hasattr
# print(hasattr(person, 'name'))  # True
# print(hasattr(person, 'age'))

#settr
setattr(person,"Johny", 12)
print(hasattr(person,"Johny"))
print(person.Johny)
print(person.money)

#delattr()
delattr(person,"money")
print(hasattr(person,"money"))





