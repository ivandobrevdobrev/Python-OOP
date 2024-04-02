from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST = 3.5
    AMOUNT = 50_000.0

    def __init__(self):
        super().__init__(self.INTEREST, self.AMOUNT)

    def increase_interest_rate(self):
        self.INTEREST += 0.5
