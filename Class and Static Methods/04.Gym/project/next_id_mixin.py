class NextIdMixin:
    id = 0 # not needed, just typed to avoid the warnings in the methods below,

    @classmethod
    def get_next_id(cls):
        return cls.id  # тука ще върне id от класа наследника. т.е ако сме в класа Customer, от там идваме да изпълним
    # метода и той ще върне  ст-ста на id която е като клса атрибут в Customer

    @classmethod
    def increment_id(cls):
        cls.id += 1