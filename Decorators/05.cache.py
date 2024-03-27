def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):
            wrapper.log[num] = func(num)
        return wrapper.log[num]

    wrapper.log = {}  # закачаме речник на wrapper , named log в, който ще пазим стойностите които връща ф-ята
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
print(fibonacci.log)
