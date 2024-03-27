from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()  # gives current time in Seconds
        func(*args, **kwargs)  # execute function
        end_time = time()  # gives current time

        return end_time - start_time  # check how long it takes for the function to be executed

    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())




