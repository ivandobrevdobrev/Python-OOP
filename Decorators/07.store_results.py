def store_results(func):
    def wrapper(*args, **kwargs):
        with open("files/log.txt", "a") as log_file:
            log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")

    return wrapper
@store_results
def sum_nums(a, b):
    return a + b

# Using class
class store_res:
    def __init__(self, func): # this is decorator
        self.func = func

    def __call__(self, *args, **kwargs):   # this is the wrapper
        with open("files/log.txt", "a") as log_file:
            log_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n")


@store_res
def summing_nums(c, d):
    return c + d

# using class with parameter given in the glass

class store_with_param():
    _DIR = "files"
    def __init__(self,file_name: str): # here comes our pararmeter
        self.file_name = file_name

    def __call__(self,func): # this is pur decorator
        def wrapper(*args,**kwargs): # this is wrapper
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(f"Function {func.__name__} was called. Result: {func(*args, **kwargs)}\n")
        return wrapper

@store_with_param("results.txt")
def summ(h, k):
    return h + k

sum_nums(5, 8)
summing_nums(12,18)
summ(10,20)
