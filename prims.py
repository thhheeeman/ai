import sys

def prims(graph, V):
    selected = [False] * V
    selected[0] = True
    total_cost = 0

    print("Edge : Weight")

    for i in range(V - 1):
        minimum = sys.maxsize
        x = y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x, y = i, j

     
        print(x, "-", y, ":", graph[x][y])

        total_cost += graph[x][y]
        selected[y] = True

    print("Total Cost =", total_cost)

# Example graph (Adjacency Matrix)
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prims(graph, 5)
