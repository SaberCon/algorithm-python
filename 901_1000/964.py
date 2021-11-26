from functools import cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cost = list(range(32))
        cost[0] = 2

        @cache
        def dp(i, tgt):
            if tgt == 0:
                return 0
            if tgt == 1:
                return cost[i]
            if i >= len(cost):
                return float('inf')

            n, r = divmod(tgt, x)
            return min(r * cost[i] + dp(i + 1, n), (x - r) * cost[i] + dp(i + 1, n + 1))

        return dp(0, target) - 1
