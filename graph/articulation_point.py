disc_count = 0
d = []
low = []
p = {}
visited = set()
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4]
}


def dfs():
    print()


def art_points(u=0):
    global disc_count
    visited.add(u)
    d[u] = disc_count
    disc_count += 1
    children = 0
    for v in graph[u]:
        if v not in visited:
            p[v] = u
            children += 1
            art_points(v)
            low[v]

        elif v != p[u]:
            low[u] = min(low[u], d[v])
