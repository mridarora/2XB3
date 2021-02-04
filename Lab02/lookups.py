import timeit
import random

def create_list(n):
    list = []
    for i in range(n):
        list.append(random.randrange(1,1000))
    return list

list = create_list(1000000)

def timetest(runs, n, list):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        list[n]
        end = timeit.default_timer()
        total += end - start
    return total/runs

for i in range(1,1000000):
    print(i-1, timetest(100, i-1, list))