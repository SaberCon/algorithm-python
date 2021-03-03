from itertools import groupby


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        return max(seats.index(1), seats[::-1].index(1),
                   max((len(list(g)) + 1) // 2 for s, g in groupby(seats) if not s))
