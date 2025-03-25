from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['E','F'],
    'F': ['E'],
    'E': []
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node == goal:
            print(f"Reached target node: {goal}")
            return
        
        if node not in visited:
            print(f"Visiting: {node}")
            visited.add(node)
            queue.extend(graph[node])  
            
    print("Target not found.")

bfs(graph, 'A', 'E')
