def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")  
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

g = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['F', 'E'],
    'F': ['E'],
    'E': []
}

print("DFS Traversal:")
dfs(g, 'A')
