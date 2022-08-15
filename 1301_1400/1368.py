from collections import defaultdict, deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        signs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        m, n = len(grid), len(grid[0])
        seen = defaultdict(lambda: m + n)
        seen[0, 0] = 0
        q = deque(((0, 0, 0),))
        while q:
            c, i, j = q.popleft()
            if (i, j) == (m - 1, n - 1):
                return c
            for d, (di, dj) in enumerate(signs):
                ni, nj = i + di, j + dj
                nc = c + (d != grid[i][j] - 1)
                if 0 <= ni < m and 0 <= nj < n and seen[ni, nj] > nc:
                    seen[ni, nj] = nc
                    if nc == c:
                        q.appendleft((nc, ni, nj))
                    else:
                        q.append((nc, ni, nj))
        raise AssertionError()
