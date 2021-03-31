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
                distance[j][k] = min(distance[j][k],distance[j][i] + distance[i][k])
    return distance

def all_pairs_bellman_ford(G):
    number_of_vertices = G.number_of_nodes()
    ans = []
    nodes = list(G.adj.keys())
    for i in nodes:
        distance = [float("inf")] * number_of_vertices
        previous = [float(0)] * number_of_vertices
        distance[i] = 0
        for j in range(0, len(nodes) - 1):
            for x in range(0, len(nodes)):
                for y in range(0, len(e)):
                    w = float(e[x][y])
                    temporary_distance = distance[x] + w
                    if temporary_distance < distance[y]:
                        distance[x] = temporary_distance
        ans.append(distance)
    for m in nodes:
        if ans[m][m] < 0:
            return [[0,0]]
    return ans
    