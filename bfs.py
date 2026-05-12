from collections import deque

def bfs(graph, start):

    visited = []
    queue = deque()

    visited.append(start)
    queue.append(start)

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Function Call
bfs(graph, 'A')