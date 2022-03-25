from functools import cache


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def max_leaf(l, r):
            if l + 1 == r:
                return arr[l]
            return max(arr[l], max_leaf(l + 1, r))

        @cache
        def min_cost(l, r):
            if l + 1 == r:
                return 0
            return min(max_leaf(l, i) * max_leaf(i, r) + min_cost(l, i) + min_cost(i, r) for i in range(l + 1, r))

        return min_cost(0, len(arr))
