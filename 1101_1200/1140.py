from functools import cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        stones = [0] * (N + 1)
        for i, n in enumerate(reversed(piles)):
            stones[i + 1] = stones[i] + n

        @cache
        def dp(n, m):
            if n <= 2 * m:
                return stones[n]
            return max(stones[n] - dp(n - i, max(m, i)) for i in range(1, 2 * m + 1))

        return dp(N, 1)
