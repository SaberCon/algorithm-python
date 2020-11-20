class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        last_dp, dp = [0] * len(s), [1] * len(s)
        for i in range(1, len(s)):
            new_dp = dp.copy()
            for j in range(0, len(s) - i):
                if s[j] == s[j + i]:
                    new_dp[j] = 2 + last_dp[j + 1]
                else:
                    new_dp[j] = max(dp[j], dp[j + 1])
            last_dp = dp
            dp = new_dp
        return dp[0]
