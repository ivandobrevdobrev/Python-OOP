from unittest import TestCase,main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Ivan","tiger","roar")

    def test_if_init_is_correct(self):
        self.assertEqual("Ivan", self.mammal.name)
        self.assertEqual("tiger", self.mammal.type)
        self.assertEqual("roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_if_animal_makes_correct_sound(self):
        self.assertEqual("Ivan makes roar",self.mammal.make_sound())

    def test_get_kingdom_correctly(self):
        self.assertEqual("animals", self.mammal.get_kingdom())


    def test_info_returns_name_and_type_of_the_animal(self):
        self.mammal.info()
        self.assertEqual("Ivan is of type tiger",self.mammal.info())



if __name__ == "__main__":
    main()