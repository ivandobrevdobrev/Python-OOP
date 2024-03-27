from itertools import permutations


def possible_permutations(elements):
    for element in permutations(elements):
        yield list(element)
[print(n) for n in possible_permutations([1, 2, 3])]