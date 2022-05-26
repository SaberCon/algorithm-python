from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    dfs(i + di, j + dj)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        return ans
