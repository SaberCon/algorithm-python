from math import gcd
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        d = nums[0]
        for n in nums:
            d = gcd(d, n)
            if d == 1:
                return True
        return False
