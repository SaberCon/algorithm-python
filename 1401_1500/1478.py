from functools import cache
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        @cache
        def min_distance(start: int, end: int) -> int:
            return 0 if start >= end else houses[end] - houses[start] + min_distance(start + 1, end - 1)

        @cache
        def dp(i: int, k: int) -> int:
            if n - i <= k:
                return 0
            if k == 1:
                return min_distance(i, n - 1)
            return min(min_distance(i, j - 1) + dp(j, k - 1) for j in range(i + 1, n))

        return dp(0, k)
