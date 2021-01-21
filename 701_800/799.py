class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured, 0]
        for i in range(query_row):
            dp = [max((dp[j - 1] - 1) / 2, 0) + max((dp[j] - 1) / 2, 0) for j in range(i + 2)] + [0]
        return min(dp[query_glass], 1)
