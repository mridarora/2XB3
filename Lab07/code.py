def test(k, c, f):
    temp = 0
    for _ in range(50):
        if(create_random_graph(k,c,f)):
            temp += 1
    return temp/50

def create_random_graph(k,c,f):
    graph = Graph(k)
    for _ in range(c):
        graph.add_edge(random.randrange(0, k),random.randrange(0, k))
    return f(graph)

for i in range(0,300):
    print(i,test(100,i,is_connected))