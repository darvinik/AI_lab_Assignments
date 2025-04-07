from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': ['E', 'F'],
    'F': ['E'],
    'E': []
}

def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    # Initialize frontiers and visited nodes
    front_start = deque([start])
    front_goal = deque([goal])
    visited_start = {start: None}
    visited_goal = {goal: None}

    while front_start and front_goal:
        # Expand from start side
        meet_node = expand_frontier(graph, front_start, visited_start, visited_goal)
        if meet_node:
            return build_path(meet_node, visited_start, visited_goal)

        # Expand from goal side
        meet_node = expand_frontier(reverse_graph(graph), front_goal, visited_goal, visited_start)
        if meet_node:
            return build_path(meet_node, visited_start, visited_goal)

    return None  # No path found

def expand_frontier(graph, frontier, visited_this_side, visited_other_side):
    current = frontier.popleft()
    for neighbor in graph.get(current, []):
        if neighbor not in visited_this_side:
            visited_this_side[neighbor] = current
            frontier.append(neighbor)
            if neighbor in visited_other_side:
                return neighbor
    return None

def reverse_graph(graph):
    rev = {node: [] for node in graph}
    for src in graph:
        for dst in graph[src]:
            rev[dst].append(src)
    return rev

def build_path(meet_node, visited_start, visited_goal):
    # Build path from start to meet_node
    path_start = []
    node = meet_node
    while node:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()

    # Build path from meet_node to goal
    path_goal = []
    node = visited_goal[meet_node]
    while node:
        path_goal.append(node)
        node = visited_goal[node]

    return path_start + path_goal

# Run the search
path = bidirectional_search('A', 'E')
print(f"Bi-Directional Path: {' -> '.join(path)}")
