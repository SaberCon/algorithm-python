from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(n, target):
            if n == 0 and target == 0:
                return 1
            if n == 0 or target == 0:
                return 0
            return sum(dp(n - 1, target - i) for i in range(1, min(target, k) + 1)) % MOD

        return dp(n, target)
