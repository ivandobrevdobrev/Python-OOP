from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST = 1.5
    AMOUNT = 2_000.0

    def __init__(self):
        super().__init__(self.INTEREST, self.AMOUNT)

    def increase_interest_rate(self):
        self.INTEREST += 0.2
