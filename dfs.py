def dfs(graph, start, goal):
    visited = set()
    visit_order = []

    def dfs_util(node, path):
        visited.add(node)
        visit_order.append(node)

        if node == goal:
            print("Visited Nodes:", visit_order)
            print("Path:", path)
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_util(neighbor, path + [neighbor]):
                    return True
        return False

    if not dfs_util(start, [start]):
        print("Goal not found")

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

dfs(graph, 'A', 'G')