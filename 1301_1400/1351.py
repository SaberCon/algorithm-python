from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neg = ans = 0
        for i in range(m):
            while neg < n and grid[i][-1 - neg] < 0:
                neg += 1
            ans += neg
        return ans
