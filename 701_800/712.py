class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1] + ord(s1[i]), dp[i + 1][j] + ord(s2[j]))
        return dp[-1][-1]
