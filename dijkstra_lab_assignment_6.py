import heapq

def d(graph, src):
    pq = []
    heapq.heappush(pq, (0, src))
    
    dist = {n: float('inf') for n in graph}
    dist[src] = 0
    
    while pq:
        d_cur, n_cur = heapq.heappop(pq)
        
        for n, w in graph[n_cur]:
            d_new = d_cur + w
            if d_new < dist[n]:
                dist[n] = d_new
                heapq.heappush(pq, (d_new, n))
        
    return dist

g = {
    'A': [('B', 10), ('C', 15)],
    'B': [('D', 12), ('F', 15)],
    'C': [('E', 10)],
    'D': [('F', 1), ('E', 2)],
    'F': [('E', 5)],
    'E': []
}

src = 'A'
res = d(g, src)
print("Shortest paths from A:", res)

