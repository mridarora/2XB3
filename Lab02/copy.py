import timeit
import random

def create_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(1,1000))
    return list

def copy(list):
    a = list.copy()

def timetest(runs, n):
    total = 0
    for _ in range(runs):
        list = create_list(n)
        start = timeit.default_timer()
        copy(list)
        end = timeit.default_timer()
        total += end - start
    return total/runs

for i in range(1,500):
    print(i*10, timetest(20, i*10))
