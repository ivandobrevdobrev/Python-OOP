def type_check(expected_symbol):
    def decorator(func):
        def wrapper(sym):
            if not isinstance(sym,expected_symbol):
                return "Bad Type"
            return func(sym)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2

print(times2(2))
print(times2('Not A Number'))
