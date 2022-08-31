from functools import cache
from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)

        @cache
        def dp(start: int, end: int, num: int) -> int:
            if start >= end or num <= 0:
                return 0
            return max(slices[start] + dp(start + 2, end, num - 1), dp(start + 1, end, num))

        return max(dp(0, n - 1, n // 3), dp(1, n, n // 3))
