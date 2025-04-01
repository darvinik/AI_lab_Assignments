import math

def alphabeta(node, depth, alpha, beta, is_max, values):
    if depth == 0 or node not in values:  # Terminal node
        return values.get(node, math.inf), [node]

    if is_max:
        best_val, best_path = -math.inf, []
        for child in values[node]:
            val, path = alphabeta(child, depth-1, alpha, beta, False, values)
            if val > best_val:
                best_val, best_path = val, [node] + path
            alpha = max(alpha, best_val)
            if alpha >= beta:  # Pruning condition
                break
        return best_val, best_path
    else:
        best_val, best_path = math.inf, []
        for child in values[node]:
            val, path = alphabeta(child, depth-1, alpha, beta, True, values)
            if val < best_val:
                best_val, best_path = val, [node] + path
            beta = min(beta, best_val)
            if beta <= alpha:  # Pruning condition
                break
        return best_val, best_path

# Game Tree (Figure 1)
fig1 = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

# Run Alpha-Beta Pruning
opt_val, opt_path = alphabeta('A', 2, -math.inf, math.inf, True, fig1)

print("Optimal Value:", opt_val)
print("Optimal Path:", " -> ".join(opt_path))
