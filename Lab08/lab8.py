import math
import timeit
import random

class MinHeap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.map = {}
        for i in range(len(L)):
            self.map[L[i].value] = i
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        smallest_known = i
        if self.left(i) < self.length and self.data[self.left(i)].key < self.data[i].key:
            smallest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)].key < self.data[smallest_known].key:
            smallest_known = self.right(i)
        if smallest_known != i:
            self.data[i], self.data[smallest_known] = self.data[smallest_known], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[smallest_known].value] = smallest_known
            self.sink(smallest_known)

    def insert(self, element):
        if len(self.data) == self.length:
            self.data.append(element)
        else:
            self.data[self.length] = element
        self.map[element.value] = self.length
        self.length += 1
        self.swim(self.length - 1)

    def insert_elements(self, L):
        for element in L:
            self.insert(element)

    def swim(self, i):
        while i > 0 and self.data[i].key < self.data[self.parent(i)].key:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[self.parent(i)].value] = self.parent(i)
            i = self.parent(i)

    def get_min(self):
        if len(self.data) > 0:
            return self.data[0]
  
    def extract_min(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.map[self.data[self.length - 1].value] = self.length - 1
        self.map[self.data[0].value] = 0
        min_element = self.data[self.length - 1]
        self.length -= 1
        self.map.pop(min_element.value)
        self.sink(0)
        return min_element

    def decrease_key(self, value, new_key):
        if new_key >= self.data[self.map[value]].key:
            return
        index = self.map[value]
        self.data[index].key = new_key
        self.swim(index)

    def get_element_from_value(self, value):
        return self.data[self.map[value]]

    def is_empty(self):
        return self.length == 0
    
    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

class Element:

    def __init__(self, value, key):
        self.value = value
        self.key = key

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.key) + ")"

class WeightedGraph:

    def __init__(self, n):
        self.adj = {}
        self.matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge[0] == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj[node2]:
            self.adj[node1].append((node2, weight))
            self.adj[node2].append((node1, weight))
            self.matrix[node1][node2] = weight
            self.matrix[node2][node1] = weight

    def w(self, node1, node2):
        for edge_info in self.adj[node1]:
            if node2 == edge_info[0]:
                return edge_info[1]

    def number_of_nodes(self):
        return len(self.adj)

def prim1(G):
    maximum = 9999999
    graph = G.matrix
    nodes = G.number_of_nodes()
    visited = [0] * nodes
    ans = WeightedGraph(nodes)
    edges = 0
    visited[0] = True
    # print("Edge : Weight\n")
    while (edges < nodes - 1):
        mini = maximum
        a = 0
        b = 0
        for i in range(nodes):
            if visited[i]:
                for j in range(nodes):
                    if ((not visited[j]) and graph[i][j]):  
                        if mini > graph[i][j]:
                            mini = graph[i][j]
                            a = i
                            b = j
        ans.add_edge(a,b,graph[a][b])
        # print(str(a) + "-" + str(b) + ":" + str(graph[a][b]))
        visited[b] = True
        edges += 1
    return ans

def PrimMST(G):
    V = G.number_of_nodes()  
    key = []
    parent = []
    temp = []
    minHeap = MinHeap([])
    for v in range(V):
        parent.append(-1)
        key.append(999999)
        minHeap.insert(Element(v,key[v]))
        temp.append(v)
    temp[0] = 0
    key[0] = 0
    minHeap.decrease_key(0, key[0])
    while minHeap.is_empty() == False:
        newHeapNode = minHeap.extract_min()
        u = newHeapNode.value
        for pCrawl in G.adj[u]:
            v = pCrawl[0]
            if (v in temp) and pCrawl[1] < key[v]:
                key[v] = pCrawl[1]
                parent[v] = u
                minHeap.decrease_key(v, key[v])
                temp.remove(v)
    # printArr(parent, V)

def printArr(parent, n):
    for i in range(1, n):
        print("% d - % d" % (parent[i], i))

def test(r, k, c, f):
    graph = create_random_graph(k, c, f)
    interval = 0
    for _ in range(r):
        start = timeit.default_timer()
        f(graph)
        end = timeit.default_timer()
        interval += (end - start)
    return interval/5

def create_random_graph(k,c,f):
    graph = WeightedGraph(k)
    for _ in range(c):
        graph.add_edge(random.randrange(0, k),random.randrange(0, k),random.randrange(0,50))
    return graph

for i in range(1,300):
    print(i,test(5,i,i,PrimMST))

# graph = WeightedGraph(9)
# graph.add_edge(0, 7, 8)
# graph.add_edge(0, 1, 4)
# graph.add_edge(1, 2, 8)
# graph.add_edge(1, 7, 11)
# graph.add_edge(2, 3, 7)
# graph.add_edge(2, 8, 2)
# graph.add_edge(2, 5, 4)
# graph.add_edge(3, 4, 9)
# graph.add_edge(3, 5, 14)
# graph.add_edge(4, 5, 10)
# graph.add_edge(5, 6, 2)
# graph.add_edge(6, 7, 1)
# graph.add_edge(6, 8, 6)
# graph.add_edge(7, 8, 7)
# PrimMST(graph)





# g = WeightedGraph(5)
# g.add_edge(0,1,2)
# g.add_edge(0,3,6)
# g.add_edge(1,2,3)
# g.add_edge(1,3,8)
# g.add_edge(1,4,5)
# g.add_edge(2,4,7)
# g.add_edge(3,4,9)
# print(prim1(g).adj)


# w1 = WeightedGraph(5)
# w1.add_edge(0,1,9)
# w1.add_edge(0,2,75)
# w1.add_edge(1,4,42)
# w1.add_edge(1,2,95)
# w1.add_edge(1,3,19)
# w1.add_edge(2,3,51)
# w1.add_edge(2,4,66)
# w1.add_edge(3,4,31)
# print(prim(w1).adj)

