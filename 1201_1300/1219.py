from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return 0
            current_gold = grid[i][j]
            grid[i][j] = 0
            max_gold = current_gold + max(dfs(i + di, j + dj) for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)))
            grid[i][j] = current_gold
            return max_gold

        return max(dfs(i, j) for i in range(m) for j in range(n))
