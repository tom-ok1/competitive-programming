class SegmentTree:
    """
    Args:
        size (int): セグメント木に格納する要素の数
        完全二分木にするためにnを超える最小の2^nにする
        dat ([int]): Nodeの配列(1-indexed)
    """

    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] * (2*self.size)

    def update(self, i, x):
        """
        Args:
            i (int): 更新したい要素のindex
            x (int): 更新する値
        """

        pos = i + self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1]

    def query(self, left, right):
        """
        [l, r)の中の範囲の最大値を答える
        Args:
            left (int): クエリの範囲の始まり(1-indexed)
            right (int): クエリの範囲の終わり、この値は含まれない(1-indexed)
        """

        def _query(a, b, k, left, right):
            if right <= a or b <= left:
                return 0
            elif a <= left and right <= b:
                return self.dat[k]
            else:
                mid = (left+right) // 2
                vl = _query(a, b, 2*k, left, mid)
                vr = _query(a, b, 2*k+1, mid, right)
                return vl + vr
        return _query(left, right, 1, 0, self.size)


N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

Z = SegmentTree(N)
for q in queries:
    tp, *cont = q
    if tp == 1:
        pos, x = cont
        # pos は 1-indexed で入力されるので、update 関数の引数は pos - 1 にします
        Z.update(pos - 1, x)
    if tp == 2:
        l, r = cont
        # 0-indexed の実装では、最初のセルに対応する半開区間は [0, size) です
        answer = Z.query(l - 1, r - 1)
        print(answer)
