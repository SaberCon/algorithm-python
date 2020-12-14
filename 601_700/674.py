class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count, ans = 1, 1
        for prev, curr in zip(nums, nums[1:]):
            if curr <= prev:
                count = 0
            count += 1
            ans = max(ans, count)
        return ans
