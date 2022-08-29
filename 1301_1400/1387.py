from functools import cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def power(n: int) -> int:
            if n == 1:
                return 0
            return 1 + (power(3 * n + 1) if n % 2 else power(n // 2))

        return sorted(range(lo, hi + 1), key=power)[k - 1]
