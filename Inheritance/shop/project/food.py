from project.product import Product


class Food(Product):
    DEFAULT_Qty = 15

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_Qty)
