class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            ans = min(ans, max(nums[i] + k, nums[-1] - k) - min(nums[i + 1] - k, nums[0] + k))
        return ans
