from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25


class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    def make_sound(self):
        return "Cluck"

    @property
    def gained_weight(self):
        return 0.35
