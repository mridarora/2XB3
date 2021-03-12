from collections import deque
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

def BFS2(G, node1, node2): 
    Q = [[node1]] 
    t = []
    if node1 == node2:  
        return [node1]
    while len(Q) != 0:
        p = Q.pop(0) 
        marked = p[-1] 
        if marked not in t:
            for n in G.adjacent_nodes(marked): 
                ans = list(p) 
                ans.append(n) 
                Q.append(ans) 
                if n == node2: 
                    return ans
            t.append(marked) 
    return []

def BFS3(graph, node):
    visited = set()
    Q = deque([node])
    visited.add(node)
    ans = {}
    while len(Q) != 0:
        current_node = Q.popleft()
        for neighbour in graph.adj[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                Q.append(neighbour)
                ans[neighbour] = current_node
    return ans

def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    ans = []
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        ans.append(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    ans.append(node)
                    return ans
                S.append(node)
    return []
           
def has_cycle(G): 
    marked =[False]*(G.number_of_nodes())
    for j in range(G.number_of_nodes()):
        if marked[j] == False:  
            if(has_cycle_helper(G,j,marked,-1)) == True: 
                return True
    return False

def has_cycle_helper(G,n,marked,node): 
    marked[n]= True
    for j in G.adj[n]: 
        if marked[j] == False :  
            if(has_cycle_helper(G,j,marked,n)): 
                return True
        elif node != j: 
            return True
    return False

def is_connected(G):
    for i in G.adj:
        for j in G.adj:
            if not DFS(G,i,j):
                return False
    return True

def test(k, c, f):
    temp = 0
    for j in range(k,2100,100):
        if(create_random_graph(j,c,f)):
            temp += 1
    return temp/20

def create_random_graph(k,c,f):
    graph = Graph(k)
    for _ in range(c):
        graph.add_edge(random.randrange(0, k),random.randrange(0, k))
    return f(graph)

for i in range(0,100):
    print(i,test(100,i,has_cycle))




















# graph = Graph(7)

# graph.add_edge(1,2) 
# graph.add_edge(2,4) 
# graph.add_edge(1,3) 
# graph.add_edge(3,4) 
# graph.add_edge(3,5) 
# graph.add_edge(4,5)
# graph.add_edge(4,6)   

# # print(graph.adj)
# print(has_cycle(graph))
