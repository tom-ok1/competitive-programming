# case 1
# graph = [
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0]
# ]

# case 2
# graph = [
#     [0, 1, 3],
#     [1, 0, 2],
#     [3, 2, 0]
# ]

# case 3
graph = [
    [0, 4, 2, 6],
    [4, 0, 3, 1],
    [2, 3, 0, 5],
    [6, 1, 5, 0]
]

# case 4
# graph = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [0, 1, 1, 0]
# ]

# case 5
# graph = [
#     [0, 2, 0, 0],
#     [2, 0, 3, 0],
#     [0, 3, 0, 0],
#     [0, 0, 0, 0]
# ]

n = len(graph)
key = [float('inf')] * n
key[0] = 0
visited = set()

for _ in range(n):
    min_cost = float('inf')
    min_idx = 0
    for i in range(n):
        if i not in visited and key[i] < min_cost:
            min_cost = key[i]
            min_idx = i

    visited.add(min_idx)
    for i in range(n):
        if graph[min_idx][i] > 0 and i not in visited and graph[min_idx][i] < key[i]:
            key[i] = graph[min_idx][i]


print(key)
