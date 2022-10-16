from functools import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @cache
        def dp(col1: int, col2: int, row: int) -> int:
            if col1 < 0 or col2 >= cols or row >= rows:
                return 0
            return grid[row][col1] + (grid[row][col2] if col1 != col2 else 0) \
                   + max(dp(min(i1, i2), max(i1, i2), row + 1) for i1 in range(col1 - 1, col1 + 2) for i2 in range(col2 - 1, col2 + 2))

        return dp(0, cols - 1, 0)
