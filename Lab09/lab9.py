import min_heap
import random
import timeit

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, 99999))
        dist[node] = 99999
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist

def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())
    temp = {}
    for node in nodes:
        dist[node] = 99999
        temp[node] = 0
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    if(temp[node] <= k):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        temp[node] += 1
                        pred[neighbour] = node
    return dist

def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its node as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[999999 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i,j):
                d[i][j] = G.w(i,j)
        d[i][i] = 0
    return d

def all_pairs_dijkstra(G):
    r, c = (G.number_of_nodes(), G.number_of_nodes())
    n = G.number_of_nodes()
    g = [[999999 for i in range(c)] for j in range(r)]
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] = G.w(i,j)
    distance = list(map(lambda a: list(map(lambda b: b, a)), g))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k],dist[j][i] + dist[i][k])
    return distance

# g = DirectedWeightedGraph()
# g.add_node(0)
# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)
# g.add_edge(0, 3, 1)
# g.add_edge(2, 4, 4)
# g.add_edge(0, 1, 5)
# g.add_edge(1, 2, 3)
# g.add_edge(2, 3, 2)
# print(mystery(g))


# g = DirectedWeightedGraph()
# g.add_node(0)
# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)
# g.add_node(5)
# g.add_edge(0, 1, -1)
# g.add_edge(0, 2, 4)
# g.add_edge(1, 2, 3)
# g.add_edge(1, 3, 2)
# g.add_edge(1, 4, 2)
# g.add_edge(3, 2, 5)
# g.add_edge(3, 1, 1)
# g.add_edge(4, 3, -3)

# print(bellman_ford(g, 0))
# print(bellman_ford_approx(g, 0, 2))
# print(bellman_ford_approx(g, 0, 3))


# def test1(r, n, f):
#     graph = create_random_complete_graph(n,1000)
#     interval = 0
#     for _ in range(r):
#         start = timeit.default_timer()
#         f(graph)
#         end = timeit.default_timer()
#         interval += (end - start)
#     return interval/r

# def test2(n, k, f):
#     graph = create_random_complete_graph(n,1000)
#     return total_dist(f(graph,random.randint(1,n+1),k))

# for i in range(1,100):
#     print(i,test1(10,i,mystery))
