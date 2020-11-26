class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1, 2, 4, 7]
        for i in range(4, n + 1):
            dp.append((dp[i - 1] * 2 - dp[i - 4]) % mod)

        ans = dp[n]
        for i in range(1, n + 1):
            ans = (ans + dp[i - 1] * dp[n - i]) % mod
        return ans
