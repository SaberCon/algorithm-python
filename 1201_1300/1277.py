from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[(0, 0)] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = (1 + min(dp[i - 1][j][0], dp[i - 1][j - 1][0]),
                                1 + min(dp[i][j - 1][1], dp[i - 1][j - 1][1]))
        return sum(min(x, y) for row in dp for x, y in row)
