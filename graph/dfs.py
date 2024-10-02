A = [
    [1, 2, 2, 4],
    [2, 2, 3, 4],
    [3, 1, 5],
    [4, 1, 6],
    [5, 1, 6],
    [6, 0]
]
S = []
V = set()
start_time = {}
end_time = {}
time = 0


def dfs(i):
    global time
    a = A[i]
    u = a[0]  # 現在のノードのID

    if u in V:
        return  # 既に訪問済みなら終了

    time += 1
    start_time[i] = time
    V.add(u)  # 訪問済みに追加
    S.append(u)  # スタックに現在のノードを追加

    neighbors = a[2:]

    for n in neighbors:
        if n not in V:  # 訪問していないノードに対して再帰的にDFSを行う
            dfs(n - 1)  # ノードIDは1から始まるため、インデックス用に-1する

    time += 1
    end_time[i] = time
    S.pop()  # スタックから現在のノードを削除


dfs(0)
for i in range(len(A)):
    print(f"{i+1} {start_time[i]} {end_time[i]}")
