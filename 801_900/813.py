class Solution:
    def largestSumOfAverages(self, A: [int], K: int) -> float:
        dp = [0.0] * (len(A))
        total = 0
        for i, n in enumerate(A):
            total += n
            dp[i] = total / (i + 1)
        for _ in range(K - 1):
            new_dp = dp.copy()
            for i in range(len(A)):
                total = 0
                for j in range(i):
                    total += A[i - j]
                    new_dp[i] = max(new_dp[i], dp[i - j - 1] + total / (j + 1))
            dp = new_dp
        return dp[-1]
