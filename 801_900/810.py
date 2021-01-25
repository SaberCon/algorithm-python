from functools import reduce


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(lambda x, y: x ^ y, nums) == 0 or len(nums) % 2 == 0
