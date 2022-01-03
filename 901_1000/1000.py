from functools import cache


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        IMPOSSIBLE = 1_000_000

        @cache
        def min_cost(start, end, count):
            size = end - start
            if count > size or (size - count) % (k - 1):
                return IMPOSSIBLE
            if size == 1:
                return 0
            if count == 1:
                return sum(stones[i] for i in range(start, end)) \
                       + min(min_cost(start, i, 1) + min_cost(i, end, k - 1) for i in range(start + 1, end))
            return min(min_cost(start, i, 1) + min_cost(i, end, count - 1) for i in range(start + 1, end))

        ans = min_cost(0, len(stones), 1)
        return ans if ans < IMPOSSIBLE else -1
