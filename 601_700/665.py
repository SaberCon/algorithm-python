class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        prev = nums[0]
        for i, num in enumerate(nums):
            if num >= prev:
                prev = num
                continue
            if num < prev and modified:
                return False
            modified = True
            if i < 2 or nums[i - 2] <= num:
                prev = num
        return True
