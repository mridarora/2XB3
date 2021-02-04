import timeit
import random

def random_number_generator():
    return (random.randrange(1,1000))


def timetest(n, list):
    number = random_number_generator()
    start = timeit.default_timer()
    list.append(number)
    end = timeit.default_timer()
    return (end - start)

list = []

for i in range(1,10000):
    print(i, timetest(i-1, list))