def timetest(runs, n, f):
    total = 0
    for _ in range(runs):
        L = create_random_list(n)
        h = Heap(L)
        start = timeit.default_timer()
        h.f()
        end = timeit.default_timer()
        total += end - start
    return total/runs

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L