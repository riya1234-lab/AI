from collections import deque

def bfs(graph, start, goal):
    visited = set()
    visit_order = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)
            visit_order.append(node)

            if node == goal:
                print("Visited Nodes:", visit_order)
                print("Path:", path)
                return

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

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

bfs(graph, 'A', 'G')