from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[i] = ans[i - 1] + num
        return ans
