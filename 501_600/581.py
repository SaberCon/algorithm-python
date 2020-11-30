class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = -1, -1
        for i in range(1, len(nums)):
            j = i - 1 if left == - 1 else left - 1
            while j >= 0 and nums[j] > nums[i]:
                left = j
                j -= 1
        for i in range(len(nums) - 2, -1, -1):
            j = i + 1 if right == - 1 else right + 1
            while j < len(nums) and nums[j] < nums[i]:
                right = j
                j += 1
        return right - left + 1 if left != -1 else 0
