from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self,name: str, price: float ):#grams: float ne gi slagame tuk, zshtoto gi definirame constant dolu
        super().__init__(name, price, Salmon.GRAMS)  # we will not allow to accept grams outside, they will always be 22
