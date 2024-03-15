from project.cat import Cat


class Tomcat(Cat):
    Gender = "Male"

    def __init__(self, name, age,):
        super().__init__(name, age, self.Gender)

    def make_sound(self):
        return "Hiss"