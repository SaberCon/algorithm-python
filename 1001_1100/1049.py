from functools import cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, m = len(stones), sum(stones)

        @cache
        def dp(i, t):
            if i >= n:
                return 0
            return max(dp(i + 1, t), stones[i] + dp(i + 1, t - stones[i]) if stones[i] <= t else 0)

        return m - 2 * dp(0, m // 2)
