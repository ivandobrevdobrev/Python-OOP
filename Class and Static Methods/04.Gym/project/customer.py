from project.next_id_mixin import NextIdMixin


class Customer(NextIdMixin):
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()   # викаме метода от наследения клас, и оотам ни връщам id което е клас атрибут тука
        self.increment_id()  # след акто сме взели ID , го увеличаваме, и следващия клиент ще получи друго ID, id ще се увеличи тука горе, просто метода е друг клас

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
