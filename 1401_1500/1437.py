from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = [i for i, n in enumerate(nums) if n]
        return len(ones) < 1 or all(i2 - i1 > k for i1, i2 in zip(ones, ones[1:]))
