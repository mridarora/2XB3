from collections import deque

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
        print(Q)
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
        print(Q)
        p = Q.pop(0) 
        marked = p[-1] 
        if marked not in t: 
            neighbour = G.adjacent_nodes(marked)
            for n in neighbour: 
                ans = list(p) 
                ans.append(n) 
                Q.append(ans) 
                if n == node2: 
                    return ans
            t.append(marked) 
    return []

def BFS3(graph, root):
    visited = set()
    Q = deque([root])
    visited.add(root)
    while Q:
        vertex = Q.popleft()
        print(vertex)
        # print(str(vertex) + " ", end="")
        for neighbour in graph.adj[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                Q.append(neighbour)
                return list(Q)
    return []

#Depth First Search
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


def DFS2(graph, node1, node2):
    Q = [[node1]]
    marked = {}
    

# def BFS3(graph, start):
#     visited, queue = set(), [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited

# def DFS3(graph,start,visited=None):

    # where_to_go_next = deque()
    # where_to_go_next.append(origin)
    # already_visited = []

    # while len(where_to_go_next) != 0:
    #     current_node = where_to_go_next.pop()
    #     print(current_node)
    #     already_visited.append(current_node)
    #     neighbours = graph[current_node]
    #     for neighbour in neighbours:
    #         if neighbour not in already_visited:
    #             where_to_go_next.append(neighbour)

    # if source is None or source not in graph.adj:
    #        return "Invalid input"
    # path = []
    # stack = [source]
    # while(len(stack) != 0):
    #     s = stack.pop()
    #     if s not in path:
    #         path.append(s)
    #     # if s not in graph.adj:
    #     #     continue
    #     for neighbor in graph.adj[s]:
    #         stack.append(neighbor)
    # return " ".join(path)

def isCyclicUtil(G,v,visited,parent): 
    visited[v]= True
    for i in G.adj[v]: 
        if visited[i]==False :  
            if(isCyclicUtil(G,i,visited,v)): 
                return True
        elif parent!=i: 
            return True
    return False
           
def isCyclic(G): 
    visited =[False]*(G.number_of_nodes())
    for i in range(G.number_of_nodes()):
        if visited[i] ==False:  
            if(isCyclicUtil(G,i,visited,-1)) == True: 
                return True
    return False

def is_connected(G):
    for i in G.adj:
        for j in G.adj:
            if not DFS(G,i,j):
                return False
    return True

graph = Graph(7)
graph.add_edge(1,4) 
graph.add_edge(4,5) 
graph.add_edge(4,2) 
graph.add_edge(4,3) 
# graph.add_edge(4,2)
graph.add_edge(5,6)   
print(graph.adj)
print(is_connected(graph))
