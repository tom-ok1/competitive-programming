import heapq


def dijkstra(A, start=0):
    n = len(A)
    S = list(range(n))
    d = [float('inf')] * n  # 頂点iにおける最短距離の和
    d[start] = 0

    while True:
        min_distance = float('inf')
        u = -1
        for i in S:
            if d[i] < min_distance:
                min_distance = d[i]
                u = i
        if u == -1:
            break

        S.remove(u)
        row = A[u]
        k = row[1]
        for i in range(k):
            v = row[2+2*i]
            w = row[2+2*i+1]
            if v in S and d[u] + w < d[v]:
                d[v] = d[u] + w
    return d


def optimized_dijkstra(A, start=0):
    n = len(A)
    visited = set()
    d = [float('inf')] * n  # 頂点iにおける最短距離の和
    d[start] = 0
    hq = [(0, start)]  # (距離, 頂点ID)となるヒープキュー

    while hq:
        _, u = heapq.heappop(hq)
        if u in visited:
            continue
        visited.add(u)
        row = A[u]
        k = row[1]
        for i in range(k):
            v = row[2+2*i]
            w = row[2+2*i+1]
            if v not in visited and d[u] + w < d[v]:
                d[v] = d[u] + w
                heapq.heappush(hq, (d[v], v))
    return d


A = [
    [0, 3, 2, 3, 3, 1, 1, 2],
    [1, 2, 0, 2, 3, 4],
    [2, 3, 0, 3, 3, 1, 4, 1],
    [3, 4, 2, 1, 0, 1, 1, 4, 4, 3],
    [4, 2, 2, 1, 3, 3,]
]

d1 = dijkstra(A)
d2 = optimized_dijkstra(A)
print(*d1)
print(*d2)
