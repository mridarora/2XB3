# Corrected number_of_nodes method of Graph class correctly
# def number_of_nodes(self):
#         return len(self.adj)

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

def DFS3(G, node1):
    S = [node1]
    marked = {}
    ans = []
    t = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        ans.append(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                ans.append(node)
                if not marked[node]:
                    t[node] = current_node
                S.append(node)
    return t
           
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