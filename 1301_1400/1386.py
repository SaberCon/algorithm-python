from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(lambda: 0)
        for i, j in reservedSeats:
            reserved[i] |= 1 << (j - 1)

        def max_seat(mask: int) -> int:
            if not mask & 0b111111110:
                return 2
            for k in (1, 3, 5):
                if not mask & (0b1111 << k):
                    return 1
            return 0

        return 2 * n - sum(2 - max_seat(mask) for mask in reserved.values())
