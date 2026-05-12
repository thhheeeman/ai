def dfs(graph, node, visited):

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []

print("DFS Traversal:")
dfs(graph, 'A', visited)