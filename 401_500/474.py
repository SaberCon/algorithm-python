class Solution:
    def findMaxForm(self, strs: [str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            count_0 = s.count('0')
            count_1 = len(s) - count_0
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i - count_0 >= 0 and j - count_1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - count_0][j - count_1] + 1)
        return dp[m][n]
