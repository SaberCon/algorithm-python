class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) // 2):
            if nums[2 * i] == nums[2 * i + 1]:
                return nums[2 * i]
        return nums[0] if nums[0] == nums[2] or nums[0] == nums[3] else nums[1]
