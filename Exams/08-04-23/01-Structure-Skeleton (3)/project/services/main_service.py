from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    def details(self) -> str:
        return f"{self.name} Main Service:\n"\
               f"Robots: {self._get_names()}"
