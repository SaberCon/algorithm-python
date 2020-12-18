class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [0] * (len(nums) + 1 - k)
        sums[0] = sum(nums[0:k])
        for i in range(len(sums) - 1):
            sums[i + 1] = sums[i] - nums[i] + nums[i + k]

