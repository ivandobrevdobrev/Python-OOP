from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []  # list of object

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:  # pishem .name za da vzemem imeto na obekta "product" kato string
                return product  # return as object

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
