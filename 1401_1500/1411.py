from functools import cache


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp_2(i: int) -> int:
            if i == 1:
                return 6
            return (dp_2(i - 1) * 3 + dp_3(i - 1) * 2) % MOD

        @cache
        def dp_3(i: int) -> int:
            if i == 1:
                return 6
            return (dp_2(i - 1) * 2 + dp_3(i - 1) * 2) % MOD

        return (dp_2(n) + dp_3(n)) % MOD
