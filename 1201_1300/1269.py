from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dp(pos: int, steps: int) -> int:
            if pos < 0 or pos >= arrLen or pos > steps:
                return 0
            if pos == steps:
                return 1
            return (dp(pos, steps - 1) + dp(pos + 1, steps - 1) + dp(pos - 1, steps - 1)) % MOD

        return dp(0, steps)
