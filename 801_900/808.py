class Solution:
    def soupServings(self, N: int) -> float:
        n = (N + 24) // 25
        if n >= 500:
            return 1.0
        memo = {}

        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if b <= 0:
                return 0.0
            if a <= 0:
                return 1.0
            if (a, b) not in memo:
                memo[a, b] = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
            return memo[a, b]

        return dp(n, n)
