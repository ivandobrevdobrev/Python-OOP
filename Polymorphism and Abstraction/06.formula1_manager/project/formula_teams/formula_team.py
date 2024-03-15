from abc import ABC, abstractmethod



class FormulaTeam(ABC):
    MIN_BUDGET = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses_for_one_race(self):
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for sponsor in self.sponsors.values(): # [{1: 1_000_000, 3: 500_000},{5: 1000_000, 7: 50_000}]
            for pos in sponsor: #{1: 1_000_000, 3: 500_000}
                if race_pos <= pos:  # sravnqwame s race_pos s 1 and 3
                    revenue += sponsor[pos]
                    break
        revenue -= self.expenses_for_one_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
