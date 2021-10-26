class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        dp = matrix[-1]
        for i in range(N - 2, -1, -1):
            dp = [matrix[i][j] + min(dp[k] for k in range(max(j - 1, 0), min(j + 2, N))) for j in range(N)]
        return min(dp)
