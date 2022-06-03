from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x_count, y_count = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    x_count[i] += 1
                    y_count[j] += 1
        return sum(x_count[i] > 1 or y_count[j] > 1 for i in range(m) for j in range(n) if grid[i][j])
