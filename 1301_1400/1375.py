from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = m = 0
        for i, n in enumerate(flips):
            m = max(m, n)
            if m == i + 1:
                ans += 1
        return ans
