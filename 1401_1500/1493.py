from itertools import groupby
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pre = ans = 0
        for b, bs in groupby(nums):
            size = sum(1 for _ in bs)
            if b:
                ans = max(ans, pre + size)
                pre = size
            elif size > 1:
                pre = 0
        return min(ans, len(nums) - 1)
