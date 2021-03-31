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