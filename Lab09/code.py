# Testing for runtime
def test1(r, n, f):
    graph = create_random_complete_graph(n,1000)
    interval = 0
    for _ in range(r):
        start = timeit.default_timer()
        f(graph,random.randint(1,n+1))
        end = timeit.default_timer()
        interval += (end - start)
    return interval/5

def test2(r, n, k, f):
    graph = create_random_complete_graph(n,1000)
    interval = 0
    for _ in range(r):
        start = timeit.default_timer()
        f(graph,random.randint(1,n+1),k)
        end = timeit.default_timer()
        interval += (end - start)
    return interval/5

for i in range(1,100):
    print(i,test1(5,100,bellman_ford),test2(5,100,i,bellman_ford_approx))


# Testing for total distance 
def test1(n, f):
    graph = create_random_complete_graph(n,1000)
    return total_dist(f(graph,random.randint(1,n+1)))

def test2(n, k, f):
    graph = create_random_complete_graph(n,1000)
    return total_dist(f(graph,random.randint(1,n+1),k))

for i in range(1,100):
    print(i,test1(100,bellman_ford),test2(100,i,bellman_ford_approx))

# Testing for mystery function
def test1(r, n, f):
    graph = create_random_complete_graph(n,1000)
    interval = 0
    for _ in range(r):
        start = timeit.default_timer()
        f(graph)
        end = timeit.default_timer()
        interval += (end - start)
    return interval/r

for i in range(1,100):
    print(i,test1(10,i,mystery))