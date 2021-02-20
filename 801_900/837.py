class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        size = min(N + 1, K + W)
        dp = [0.0] * size
        dp[0] = total = 1.0
        for i in range(1, size):
            if i > W:
                total -= dp[i - W - 1]
            dp[i] = total / W
            if i < K:
                total += dp[i]
        return sum(dp[K:])
