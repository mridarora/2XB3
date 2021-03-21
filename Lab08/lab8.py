#Undirected graph using an adjacency list
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
    print("Edge : Weight\n")
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
        print(str(a) + "-" + str(b) + ":" + str(graph[a][b]))
        visited[b] = True
        edges += 1
    return ans

g = WeightedGraph(5)
g.add_edge(0,1,2)
g.add_edge(0,3,6)
g.add_edge(1,2,3)
g.add_edge(1,3,8)
g.add_edge(1,4,5)
g.add_edge(2,4,7)
g.add_edge(3,4,9)
print(prim1(g).adj)


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

