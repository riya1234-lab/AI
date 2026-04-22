def minimax(node, is_max, tree, visited):
    visited.append(node)

    if isinstance(node, int):
        return node, [node]

    if is_max:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, False, tree, visited)
            if value > best_value:
                best_value = value
                best_path = [node] + path
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, True, tree, visited)
            if value < best_value:
                best_value = value
                best_path = [node] + path
        return best_value, best_path


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [7, 6]
}

visited_nodes = []
optimal_value, optimal_path = minimax('A', True, tree, visited_nodes)

print("Optimal value at root node A:", optimal_value)
print("Optimal path:", " -> ".join(map(str, optimal_path)))
print("Visited nodes:", visited_nodes)