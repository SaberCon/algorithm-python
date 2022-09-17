from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        total = 0
        for num in nums:
            total += num
            ans = max(ans, 1 - total)
        return ans
