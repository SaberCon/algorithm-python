from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i1: int, i2: int) -> int:
            if i1 >= len(nums1) or i2 >= len(nums2):
                return -1000000
            return max(nums1[i1] * nums2[i2] + max(dp(i1 + 1, i2 + 1), 0), dp(i1, i2 + 1), dp(i1 + 1, i2))

        return dp(0, 0)
