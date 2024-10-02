from collections import deque

A = [
    [1, 2, 2, 4],
    [2, 1, 4],
    [3, 0],
    [4, 1, 3]
]

d = [0] * 4
q = deque()
visited = set()


q.append(A[0][0])
visited.add(A[0][0])
while q:
    u = q.popleft()
    row = A[u-1]
    neighbors = row[2:]

    for n in neighbors:
        if n not in visited:
            visited.add(n)
            d[n-1] = d[u-1] + 1
            q.append(n)


print(*d)
