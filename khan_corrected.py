from collections import deque

def khan_topological_sort(graph, v):
    # Initialize in-degree for all vertices
    in_degree = [0] * v

    # Calculate in-degrees
    for u in graph:
        for neighbor in graph[u]:
            in_degree[neighbor] += 1

    # Initialize the queue with all vertices having in-degree 0
    queue = deque([u for u in range(v) if in_degree[u] == 0])

    topological_order = []

    # Process vertices in topological order
    while queue:
        node = queue.popleft()
        topological_order.append(node)

        for neighbor in graph.get(node, []):  # Use graph.get() for safety
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If topological order contains all vertices, return it
    if len(topological_order) == v:
        return topological_order
    else:
        return "Cycle Detected"

# Test graph
graph = {
    0: [1],
    1: [2, 4],
    2: [5, 3],
    3: [5, 6],
    4: [2, 5, 3],
    5: [6],
    6: []
}

print(khan_topological_sort(graph, 7))

# Issues fixed: 
# What if v > len(graph)?
# "cycle Detected" was incorrectly implemented
# There was an early return? It may cause the program to terminate earlier than needed.

