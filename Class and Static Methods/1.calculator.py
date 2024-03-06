from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums) -> int:  # sums all the arguments passed to the function and returns the result
        return sum(nums)

    @staticmethod
    def multiply(*nums) -> int:
        return reduce(lambda x, y: x * y, nums)

    @staticmethod
    def subtract(*nums) -> int:
        return reduce(lambda x, y: x - y, nums)

    @staticmethod
    def divide(*nums) -> float:
        return reduce(lambda x, y: x / y, nums)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
