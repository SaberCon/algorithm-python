from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])

        @cache
        def apples(row: int, col: int) -> int:
            return (pizza[row][col] == 'A') + apples(row, col + 1) + apples(row + 1, col) - apples(row + 1, col + 1) \
                if row < rows and col < cols else 0

        @cache
        def dp(row: int, col: int, num: int) -> int:
            if rows - row + cols - col - 1 < num:
                return 0
            if num == 1:
                return int(apples(row, col) > 0)
            return (sum(dp(i, col, num - 1) for i in range(row + 1, rows) if apples(row, col) - apples(i, col) > 0) +
                    sum(dp(row, j, num - 1) for j in range(col + 1, cols) if apples(row, col) - apples(row, j) > 0)) \
                % 1000000007

        return dp(0, 0, k)
