from functools import cache


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def max_sum(start, end):
            if start + k >= end:
                return max(arr[start:end]) * (end - start)
            return max(max_sum(start, i) + max_sum(i, end) for i in range(start + 1, start + k + 1))

        return max_sum(0, len(arr))
