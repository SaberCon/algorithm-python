class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] + [0] * k
        for i in range(n):
            new_dp = dp.copy()
            for j in range(1, k + 1):
                new_dp[j] += new_dp[j - 1]
                if j > i:
                    new_dp[j] -= dp[j - i - 1]
                new_dp[j] %= mod
            dp = new_dp
        return dp[k]
