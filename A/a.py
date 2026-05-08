from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        q = deque([(0, 0)])
        pacific = set()
        pacific.add((0, 0))
        while q:
            i, j = q.popleft()
            for left, right in [(1, 0), (0, 1)]:
                ni = i + left
                mj = j + right
                if 0 <= ni < n and 0 <= mj < m and heights[ni][mj] >= heights[i][j]:
                    q.append((ni, mj))
                    pacific.add((ni, mj))
        q = deque([(n - 1, m - 1)])
        ans = []
        while q:
            i, j = q.popleft()
            for left, right in [(-1, 0), (0, -1)]:
                ni = i + left
                mj = j + right
                if 0 <= ni < n and 0 <= mj < m and heights[ni][mj] >= heights[i][j]:
                    q.append((ni, mj))
                    if (ni, mj) in pacific:
                        ans.append([ni, mj])

        return ans


sol = Solution()
print(
    sol.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
