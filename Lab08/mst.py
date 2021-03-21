# We modified constructor by initializing a matrix and also 
# modified add_edge function as shown below.

# def __init__(self, n):
#     self.adj = {}
#     self.matrix = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         self.adj[i] = []

# def add_edge(self, node1, node2, weight):
#     if node1 not in self.adj[node2]:
#         self.adj[node1].append((node2, weight))
#         self.adj[node2].append((node1, weight))
#         self.matrix[node1][node2] = weight
#         self.matrix[node2][node1] = weight

def prim1(G):
    maximum = 9999999
    graph = G.matrix
    nodes = G.number_of_nodes()
    visited = [0] * nodes
    ans = WeightedGraph(nodes)
    edges = 0
    visited[0] = True
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
        visited[b] = True
        edges += 1
    return ans