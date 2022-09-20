from functools import cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(size: int, cost: int, top: int) -> int:
            if cost < 0:
                return 0
            if size == 0:
                return 1 if cost == 0 else 0
            if top == m:
                return m * dp(size - 1, cost, top) % MOD
            return (dp(size, cost, top + 1) + top * dp(size - 1, cost, top) + dp(size - 1, cost - 1, top + 1)
                    - (top + 1) * dp(size - 1, cost, top + 1)) % MOD

        return dp(n, k, 0)
