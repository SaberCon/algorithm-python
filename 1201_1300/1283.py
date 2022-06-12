from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        mi, ma = 1, max(nums)
        while mi < ma:
            mid = (mi + ma) // 2
            if sum(ceil(num / mid) for num in nums) > threshold:
                mi = mid + 1
            else:
                ma = mid
        return mi
