class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def __init__(self, first_name, last_name,fact_number):
        super().__init__(first_name, last_name)
        #Person.__init__(self,first_name,last_name)
        self.fact_number = fact_number
    def go_to_university(self):
        return "walking to Uni"

    def get_info(self):   #населдяване на метод от Parent class - get_full_name()
        return f"{self.get_full_name()} with faculty num: {self.fact_number}"

    def get_full_name(self):  # пренаписване на метод от parent class-a
        return f"{self.last_name} {self.first_name}"


p = Person("Ivan", "Dobrev")
print(p.get_full_name())
s = Student("Pesho", "Ivanov",388)
print(s.first_name)
print(s.last_name)
print(s.get_full_name())
print(s.go_to_university())
print(s.fact_number)
print(s.get_info())