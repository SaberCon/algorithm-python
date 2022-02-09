from functools import cache


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def min_score(l, r):
            if r - l < 2:
                return 0
            if r - l == 2:
                return values[l] * values[l + 1] * values[l + 2]
            return min(values[l] * values[r] * values[i] + min_score(l, i) + min_score(i, r) for i in range(l + 1, r))

        return min_score(0, len(values) - 1)
