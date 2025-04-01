import math

# Alpha-Beta Pruning Function
def alphabeta(node, depth, alpha, beta, is_max, values):
    if depth == 0 or node not in values:  # Leaf Node
        return values.get(node, math.inf), [node]

    if is_max:
        best_val, best_path = -math.inf, []
        for child in values[node]:
            val, path = alphabeta(child, depth-1, alpha, beta, False, values)
            if val > best_val:
                best_val, best_path = val, [node] + path
            alpha = max(alpha, best_val)
            if alpha >= beta:  # Prune
                break
        return best_val, best_path
    else:
        best_val, best_path = math.inf, []
        for child in values[node]:
            val, path = alphabeta(child, depth-1, alpha, beta, True, values)
            if val < best_val:
                best_val, best_path = val, [node] + path
            beta = min(beta, best_val)
            if beta <= alpha:  # Prune
                break
        return best_val, best_path

# Figure 2 Tree Structure
fig2 = {
    'MAX': ['MIN1', 'MIN2'],
    'MIN1': ['MAX1', 'MAX2'],
    'MIN2': ['MAX3', 'MAX4'],
    'MAX1': ['L1', 'L2', 'L3'],
    'MAX2': ['L4', 'L5', 'L6'],
    'MAX3': ['L7', 'L8', 'L9'],
    'MAX4': ['L10', 'L11', 'L12'],

    'L1': 5, 'L2': -1, 'L3': 3,
    'L4': 3, 'L5': -2, 'L6': -5,
    'L7': 8, 'L8': 6, 'L9': 1,
    'L10': -4, 'L11': 2, 'L12': 7
}

# Run Alpha-Beta Pruning
opt_val, opt_path = alphabeta('MAX', 3, -math.inf, math.inf, True, fig2)

print("Optimal Value:", opt_val)
print("Optimal Path:", " -> ".join(opt_path))
