from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = total = 0
        for s in sorted(satisfaction, reverse=True):
            total += s
            if total <= 0:
                break
            ans += total
        return ans
