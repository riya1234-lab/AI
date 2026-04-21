def dfs(g, node, goal, visited, path):
    visited.append(node)
    path.append(node)

    if node == goal:
        print("Visited:", visited)
        print("Path:", path)
        return True

    # Use get() to avoid error if node not present
    for n in g.get(node, []):
        if n not in visited:
            if dfs(g, n, goal, visited, path):
                return True

    path.pop()
    return False


# Input graph
g = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(f"Enter neighbors of {node}: ").split()
    g[node] = neighbors

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

dfs(g, start, goal, [], [])