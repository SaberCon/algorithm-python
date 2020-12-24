class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        distances = [n2 - n1 for n1, n2 in zip(nums, nums[1:])]
