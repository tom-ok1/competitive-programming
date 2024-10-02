from collections import defaultdict

# 入力データ
n = 10  # ユーザー数
m = 9   # 友達関係の数

# 友達関係リスト
friendships = [
    [0, 1],
    [0, 2],
    [3, 4],
    [2, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 9],
    [3, 5]
]

# 質問の数
q = 3

# 質問リスト
queries = [
    [0, 1],  # 質問1: 0と1はたどり着けるか
    [5, 9],  # 質問2: 5と9はたどり着けるか
    [1, 3]   # 質問3: 1と3はたどり着けるか
]

graph = [[i] for i in range(n)]
group = defaultdict()

for f in friendships:
    g = graph[f[0]]
    g.append(f[1])

visited = set()


def dfs(start, group_name):
    S = [start]

    while S:
        u = S.pop()
        if u not in visited:
            visited.add(u)
            group[u] = group_name
            neighbors = graph[u][1:]
            for n in reversed(neighbors):
                if n not in visited:
                    S.append(n)


for g in graph:
    if g[0] not in visited:
        dfs(g[0], g[0])

for q in queries:
    q_left = group[q[0]]
    q_right = group[q[1]]
    if q_left == q_right:
        print("yes")
    else:
        print("no")

print(group)
