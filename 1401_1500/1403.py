from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        t = sum(nums) / 2
        for i, num in enumerate(nums):
            t -= num
            if t < 0:
                return nums[:i + 1]
