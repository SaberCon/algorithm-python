from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        r1 = r2 = ans = 0
        for left, right in sorted((i - r, i + r) for i, r in enumerate(ranges)):
            if left > r2:
                return -1
            if left > r1:
                r1 = r2
                ans += 1
            if right >= n:
                return ans + 1
            r2 = max(r2, right)
        return -1
